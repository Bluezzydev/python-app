var app = WebApplication.CreateBuilder(args).Build();

app.MapGet("/", () => new { branch = "lang/dotnet", lang = "dotnet" });
app.MapGet("/healthz", () => new { ok = true });

app.Run();
