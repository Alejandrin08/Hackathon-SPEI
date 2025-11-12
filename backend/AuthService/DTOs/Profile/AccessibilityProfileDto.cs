using System.ComponentModel.DataAnnotations;

namespace AuthService.DTOs.Profile
{
    public class AccessibilityProfileDto
    {
        public string? Alias { get; set; }
        public string? AgeRange { get; set; }
        public string? LiteracyLevel { get; set; }

        public string Theme { get; set; } = "light";
        public bool ScreenReaderMode { get; set; } = false;
        public decimal FontScale { get; set; } = 1.0m;
        public string NudgingLevel { get; set; } = "medium";
        public bool VoiceFeedback { get; set; } = false;
    }
}