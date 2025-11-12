using System.ComponentModel.DataAnnotations;

namespace AuthService.DTOs.Auth
{
    public class LoginRequestDto
    {
        [Required(ErrorMessage = "El Email es obligatorio")]
        public string Email { get; set; }

        [Required(ErrorMessage = "La contraseña es obligatoria")]
        public string Password { get; set; }
    }
}
