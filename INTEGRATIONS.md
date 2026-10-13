# Integrations

## Supported architecture

- Power BI via Power BI REST API and OAuth2/Entra ID
- Tableau via Tableau REST API
- Excel and cloud files via upload and storage connectors
- S3 and Blob connectors for scalable storage

## Design principle

Adapters are isolated from the core business logic so connectors can be added without modifying the main platform behavior.
