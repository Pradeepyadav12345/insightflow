from app.core.config import Settings


def test_settings_parses_comma_separated_lists() -> None:
    settings = Settings.model_validate(
        {
            "allowed_hosts": "localhost,127.0.0.1",
            "cors_origins": "http://localhost:3000,http://localhost:5173,http://localhost:8081",
        }
    )

    assert settings.allowed_hosts == ["localhost", "127.0.0.1"]
    assert settings.cors_origins == [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://localhost:8081",
    ]
