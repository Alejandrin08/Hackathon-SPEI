namespace AuthService.DTOs.Auth
{
    public class TokenResponseDto
    {
        public string Token { get; set; } = string.Empty;
        public int ExpiresIn { get; set; }
    }
}
