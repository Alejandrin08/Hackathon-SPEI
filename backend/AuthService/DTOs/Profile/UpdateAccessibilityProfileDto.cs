using System.ComponentModel.DataAnnotations;

namespace AuthService.DTOs.Profile
{
    public class UpdateAccessibilityProfileDto
    {
        [StringLength(100)]
        public string? Alias { get; set; }

        [StringLength(50)]
        public string? AgeRange { get; set; } 

        [StringLength(50)]
        public string? LiteracyLevel { get; set; } 

        [Required]
        public string Theme { get; set; }

        [Required]
        public bool ScreenReaderMode { get; set; } = false;

        [Required]
        [Range(0.5, 3.0)]
        public decimal FontScale { get; set; } = 1.0m;

        [Required]
        public string NudgingLevel { get; set; } = "medium";

        [Required]
        public bool VoiceFeedback { get; set; } = false;
    }
}