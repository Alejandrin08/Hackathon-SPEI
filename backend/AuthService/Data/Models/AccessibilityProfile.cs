using System;
using System.Collections.Generic;

namespace AuthService.Data.Models;

public partial class AccessibilityProfile
{
    public Guid Id { get; set; }

    public Guid UserId { get; set; }

    public string? Alias { get; set; }

    public string? AgeRange { get; set; }

    public string Theme { get; set; } = null!;

    public decimal FontScale { get; set; }

    public bool VoiceFeedback { get; set; }

    public bool ScreenReaderMode { get; set; }

    public string NudgingLevel { get; set; } = null!;

    public string? LiteracyLevel { get; set; }

    public DateTime UpdatedAt { get; set; }

    public virtual User User { get; set; } = null!;
}
