using AuthService.Data.Models;
using AuthService.DTOs.Auth;
using AuthService.Services.Contracts;
using Microsoft.AspNetCore.Identity;
using Microsoft.EntityFrameworkCore;

namespace AuthService.Services.Implementation
{
    public class AuthServiceImplementation : IAuthService
    {
        private readonly AuthDbContext _context;
        private readonly IPasswordHasher<User> _passwordHasher;
        private readonly ITokenService _tokenService;

        public AuthServiceImplementation(
            AuthDbContext context,
            IPasswordHasher<User> passwordHasher,
            ITokenService tokenService)
        {
            _context = context;
            _passwordHasher = passwordHasher;
            _tokenService = tokenService;
        }

        public async Task<User> RegisterAsync(RegisterRequestDto request)
        {
            if (!string.IsNullOrEmpty(request.Email))
            {
                var existingUserByEmail = await _context.Users
                    .FirstOrDefaultAsync(u => u.Email == request.Email);
                if (existingUserByEmail != null)
                {
                    throw new InvalidOperationException($"El email '{request.Email}' ya está registrado.");
                }
            }

            var newUser = new User
            {
                Id = Guid.NewGuid(),
                UserName = request.UserName, 
                Email = request.Email,
                PreferredLanguage = request.PreferredLanguage ?? "es-MX",
                CreatedAt = DateTime.UtcNow,
                UpdatedAt = DateTime.UtcNow
            };

            newUser.HashedPassword = _passwordHasher.HashPassword(newUser, request.Password);

            using var transaction = await _context.Database.BeginTransactionAsync();
            try
            {
                _context.Users.Add(newUser);
                await _context.SaveChangesAsync();

                var newProfile = new AccessibilityProfile
                {
                    Id = Guid.NewGuid(),
                    UserId = newUser.Id,
                    UpdatedAt = DateTime.UtcNow
                };
                _context.AccessibilityProfiles.Add(newProfile);
                await _context.SaveChangesAsync();

                await transaction.CommitAsync();

                return newUser;
            }
            catch (DbUpdateException ex)
            {
                await transaction.RollbackAsync();
                var innerMessage = ex.InnerException?.Message ?? ex.Message;
                throw new InvalidOperationException($"Error al registrar: {innerMessage}", ex);
            }
        }

        public async Task<TokenResponseDto> LoginAsync(LoginRequestDto request)
        {
            var user = await _context.Users
                .FirstOrDefaultAsync(u => u.Email == request.Email);

            if (user == null)
            {
                throw new UnauthorizedAccessException("Usuario o contraseña incorrecta.");
            }

            var passwordVerificationResult = _passwordHasher.VerifyHashedPassword(
                user,
                user.HashedPassword,
                request.Password
            );

            if (passwordVerificationResult == PasswordVerificationResult.Failed)
            {
                throw new UnauthorizedAccessException("Correo o contraseña incorrecta.");
            }

            var token = _tokenService.GenerateToken(user);

            return new TokenResponseDto
            {
                Token = token,
                ExpiresIn = 60 
            };
        }
    }
}