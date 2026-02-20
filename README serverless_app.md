# VaultMessage — E2EE Serverless Flutter Client

A Flutter mobile application that implements **end-to-end encrypted (E2EE) messaging** over a Vercel serverless backend. All cryptographic operations happen entirely on-device using RSA-2048; the server never sees plaintext.

---

## Features

- **On-device RSA-2048 key generation** — keypairs are generated locally and never transmitted in private form
- **Secure key storage** — private keys are persisted using `flutter_secure_storage` (Keychain on iOS, Keystore on Android)
- **End-to-end encryption** — messages are encrypted with the recipient's public key before leaving the device
- **Offline message queue** — if the recipient is offline, the encrypted payload is queued server-side and delivered on next login
- **Auto-routing** — the app automatically redirects to the dashboard if a local session (keypair + username) already exists
- **Material 3 dark theme** — premium dark UI built on Material 3 with an indigo color scheme

---

## Architecture Overview

```
+----------------------------------+
|         Flutter App              |
|                                  |
|  +------------+  +-------------+ |
|  |CryptoService|  | ApiService  | |
|  |            |  |             | |
|  | RSA Keygen |  | POST/GET/   | |
|  | Encrypt    |  | DELETE      | |
|  | Decrypt    |  | requests    | |
|  | SecureStore|  |             | |
|  +------------+  +------+------+ |
|                         |        |
+-------------------------+--------+
                          | HTTPS
                          v
          +---------------------------+
          |  Vercel Serverless API    |
          |                           |
          |  POST /api/register       |
          |  GET  /api/resolve-peer   |
          |  POST /api/offline-queue  |
          |  GET  /api/offline-queue  |
          |  DEL  /api/offline-queue  |
          +---------------------------+
```

---

## Project Structure

```
mobile/
├── lib/
│   ├── main.dart                    # App entry point, service wiring, theme, routing
│   ├── services/
│   │   ├── api_service.dart         # HTTP client wrapping all Vercel serverless endpoints
│   │   └── crypto_service.dart      # RSA keypair generation, encryption, decryption, secure storage
│   └── ui/
│       ├── registration_screen.dart  # First-run: generate keys, register with backend
│       ├── dashboard_screen.dart     # Peer search and offline message inbox
│       └── chat_screen.dart          # Per-peer E2EE message composition and decryption
├── pubspec.yaml
└── README.md
```

---

## Core Services

### `CryptoService`

| Method | Description |
|--------|-------------|
| `generateAndSaveKeyPair()` | Generates a 2048-bit RSA keypair and persists both keys to secure storage. Returns the public key PEM string. |
| `getPublicKey()` | Reads the locally stored RSA public key. |
| `getPrivateKey()` | Reads the locally stored RSA private key. |
| `saveUsername(username)` | Persists the registered username to secure storage. |
| `getUsername()` | Retrieves the stored username. |
| `hasKeys()` | Returns `true` if a full session (private key, public key, username) exists locally. |
| `encrypt(plainText, publicKeyPem)` | Encrypts `plainText` with the receiver's public key. Returns Base64. |
| `decrypt(encryptedBase64)` | Decrypts a Base64-encoded payload using the stored private key. |
| `clearAll()` | Wipes all keys and session data from secure storage. |

### `ApiService`

Wraps the Vercel serverless backend. Each method maps to a specific endpoint and bearer token.

| Method | Endpoint | HTTP |
|--------|----------|------|
| `registerUser(username, email, publicKey)` | `/api/register` | `POST` |
| `resolvePeer(username)` | `/api/resolve-peer?username=` | `GET` |
| `queueOfflineMessage(recipient, sender, payload)` | `/api/offline-queue` | `POST` |
| `fetchOfflineMessages(username)` | `/api/offline-queue?username=` | `GET` |
| `deleteOfflineMessage(messageId)` | `/api/offline-queue?id=` | `DELETE` |

All methods throw a typed `ApiException` on non-2xx responses.

---

## UI Screens

| Screen | File | Description |
|--------|------|-------------|
| Registration | `registration_screen.dart` | Collects username and email, generates a local RSA keypair, and calls `POST /api/register` to publish the public key |
| Dashboard | `dashboard_screen.dart` | Search for peers by username and view/decrypt offline messages queued for the current user |
| Chat | `chat_screen.dart` | Compose E2EE messages: resolves the peer's public key, encrypts the message locally, then either sends or queues it offline |

---

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `crypton` | `^2.0.1` | RSA-2048 keypair generation, encryption, and decryption |
| `flutter_secure_storage` | `^9.0.0` | OS-level secure storage for private keys (Keychain / Keystore) |
| `http` | `^1.2.1` | HTTP client for communicating with the Vercel serverless API |

---

## Getting Started

### Prerequisites

- Flutter SDK `>=3.0.0 <4.0.0`
- An active Vercel deployment of the serverless backend (or a local dev server)

### 1. Install Dependencies

```bash
flutter pub get
```

### 2. Configure the API Base URL

Open `lib/main.dart` and update the `defaultBaseUrl` constant:

```dart
// For a deployed Vercel project:
const String defaultBaseUrl = 'https://<your-vercel-project>.vercel.app';

// For Android Emulator local development:
const String defaultBaseUrl = 'http://10.0.2.2:3000';

// For iOS Simulator local development:
const String defaultBaseUrl = 'http://localhost:3000';
```

### 3. Run the App

```bash
# Android (connected device or emulator)
flutter run

# iOS Simulator
flutter run -d ios

# Web (development preview)
flutter run -d chrome
```

### 4. Build for Release

```bash
# Android APK (debug)
flutter build apk --debug

# Android APK (release)
flutter build apk --release

# iOS (requires macOS + Xcode)
flutter build ios --release
```

---

## Platform Support

| Platform | Status |
|----------|--------|
| Android | Supported |
| iOS | Supported |
| Web | Supported (development preview) |
| Windows | Supported (desktop) |

> **Note**: `flutter_secure_storage` requires Android `minSdkVersion 18` and iOS 9.0+. Ensure your platform-specific config files reflect these minimums.

---

## Security Notes

- The **private key never leaves the device**. Only the RSA public key is transmitted to the backend during registration.
- All messages are encrypted client-side before any network call is made.
- Bearer tokens used by `ApiService` are VCK tokens scoped per endpoint. In production, consider loading these from a secure config or environment-specific build flavors instead of hardcoding them in source.
- `flutter_secure_storage` uses the Android Keystore System and iOS Keychain — both hardware-backed on modern devices.

---

## Related

- [Backend README](../backend/README.md) — Vercel serverless functions, database schema, and API reference
