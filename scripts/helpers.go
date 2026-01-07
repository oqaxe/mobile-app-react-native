package helpers

import (
	"crypto/rand"
	"crypto/sha256"
	"encoding/hex"
	"errors"
	"log"
	"strings"
)

func GenerateRandomString(n int) (string, error) {
	b := make([]byte, n)
	if _, err := rand.Read(b); err != nil {
		return "", err
	}
	return hex.EncodeToString(b), nil
}

func HashString(s string) string {
	h := sha256.New()
	h.Write([]byte(s))
	return hex.EncodeToString(h.Sum(nil))
}

func ValidateEmail(email string) bool {
	if len(email) < 3 {
		return false
	}
	if !strings.Contains(email, "@") {
		return false
	}
	parts := strings.Split(email, "@")
	if len(parts) != 2 {
		return false
	}
	if len(parts[0]) < 1 || len(parts[1]) < 1 {
		return false
	}
	return true
}

func HandleError(err error) {
	if err != nil {
		log.Println(err)
	}
}

func ValidatePassword(password string) bool {
	if len(password) < 8 {
		return false
	}
	hasUpper := false
	hasLower := false
	hasNumber := false
	for _, char := range password {
		if 'A' <= char && char <= 'Z' {
			hasUpper = true
		} else if 'a' <= char && char <= 'z' {
			hasLower = true
		} else if '0' <= char && char <= '9' {
			hasNumber = true
		}
	}
	return hasUpper && hasLower && hasNumber
}

func ValidateUsername(username string) error {
	if len(username) < 3 {
		return errors.New("username must be at least 3 characters long")
	}
	if !strings.MatchString("^[a-zA-Z0-9_]+$", username) {
		return errors.New("username can only contain letters, numbers, and underscores")
	}
	return nil
}