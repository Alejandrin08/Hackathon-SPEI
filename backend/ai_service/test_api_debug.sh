#!/usr/bin/env bash

BASE_URL="http://localhost:8001/ai"

echo "=========================================="
echo "🔍 Testing /ai/health"
echo "=========================================="

HEALTH_RESPONSE=$(curl -w "\nHTTP_STATUS:%{http_code}\n" -X GET "$BASE_URL/health")
echo "$HEALTH_RESPONSE"

HTTP_CODE=$(echo "$HEALTH_RESPONSE" | grep HTTP_STATUS | cut -d':' -f2)

if [ "$HTTP_CODE" != "200" ]; then
  echo "❌ /ai/health no respondió con 200. Revisa que el servidor esté corriendo en $BASE_URL/health"
  exit 1
fi

echo -e "\n\n"

# -------------------------------------------
# 1️⃣ NUDGING
# -------------------------------------------
echo "=========================================="
echo "🟡 Testing /ai/nudge"
echo "=========================================="

curl -w "\nHTTP_STATUS:%{http_code}\n" -X POST "$BASE_URL/nudge" \
  -H "Content-Type: application/json" \
  -d '{
        "user_id": "user_001",
        "session_id": "sess_001",
        "screen": "send-money",
        "num_validation_errors": 3,
        "time_on_screen_seconds": 80,
        "num_back_navigations": 1,
        "steps_total": 3,
        "current_step": 2
      }'

echo -e "\n\n"

# -------------------------------------------
# 2️⃣ ACCESSIBILITY
# -------------------------------------------
echo "=========================================="
echo "🟢 Testing /ai/accessibility"
echo "=========================================="

curl -w "\nHTTP_STATUS:%{http_code}\n" -X POST "$BASE_URL/accessibility" \
  -H "Content-Type: application/json" \
  -d '{
        "user_id": "user_002",
        "can_read_small_text": false,
        "uses_screen_reader": true,
        "feels_confident_with_apps": "low",
        "age_range": "60_plus",
        "avg_time_per_screen_seconds": 40,
        "total_validation_errors": 2,
        "requested_help_count": 2
      }'

echo -e "\n\n"

# -------------------------------------------
# 3️⃣ RISK
# -------------------------------------------
echo "=========================================="
echo "🔴 Testing /ai/risk"
echo "=========================================="

curl -w "\nHTTP_STATUS:%{http_code}\n" -X POST "$BASE_URL/risk" \
  -H "Content-Type: application/json" \
  -d '{
        "user_id": "user_003",
        "amount": 6000.0,
        "is_new_beneficiary": true,
        "hour_of_day": 21,
        "num_past_transactions": 5,
        "avg_transaction_amount": 800.0,
        "max_transaction_amount": 2500.0,
        "num_transactions_to_beneficiary": 0,
        "is_new_device": false,
        "geolocation_changed": false
      }'

echo -e "\n\n"
echo "=========================================="
echo "✅ Tests terminados"
echo "=========================================="