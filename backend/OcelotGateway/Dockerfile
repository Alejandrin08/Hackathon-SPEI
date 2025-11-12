FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src

COPY OcelotGateway.csproj ./
RUN dotnet restore "OcelotGateway.csproj"

COPY . .
RUN dotnet publish "OcelotGateway.csproj" -c Release -o /app/publish
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS final
WORKDIR /app
COPY --from=build /app/publish .

ENV ASPNETCORE_URLS=http://+:8080
EXPOSE 8080

ENTRYPOINT ["dotnet", "OcelotGateway.dll"]
