using System.ComponentModel.DataAnnotations;

namespace AuthService.DTOs.Profile
{
    public class UpdateConsentRequestDto
    {
        [Required(ErrorMessage = "Debe indicar si acepta (true) o no (false).")]
        public bool Granted { get; set; }
    }
}