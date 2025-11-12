FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src

COPY OpenFinanceService.csproj ./
RUN dotnet restore "OpenFinanceService.csproj"

COPY . .
RUN dotnet publish "OpenFinanceService.csproj" -c Release -o /app/publish
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS final
WORKDIR /app
COPY --from=build /app/publish .

ENV ASPNETCORE_URLS=http://+:8080
EXPOSE 8080

ENTRYPOINT ["dotnet", "OpenFinanceService.dll"]
