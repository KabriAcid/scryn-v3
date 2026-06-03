# ⚙️ SCRYN v3 — GUEST PAGES PROMPT (FINAL, EXHAUSTIVE)

## 🎯 Objective

Build premium, **friendly**, production-ready **guest-facing pages** for Scryn v3:

1. **Home** (`/`) – landing page with hero, features, and CTAs  
2. **Registration** (`/register`) – business signup with mock email confirmation  
3. **Login** (`/login`) – business signin with session management  
4. **Redemption** (`/redeem`) – end‑user scratch card redemption for **data bundles only**  
5. **Success / Error** – shown inline on redemption page (no separate routes unless needed)

All pages must follow **utility‑first CSS** (Tailwind config + `global.css`), use **Radix‑based reusable components**, have **strict TypeScript types**, and implement **live validation + sanitization** with a **friendly tone**.

---

## 🧱 Technology Stack (Summary)

- **Next.js 14+** (App Router)  
- **TypeScript** (strict mode, no `any`)  
- **React 18+**  
- **Tailwind CSS** – extended via `tailwind.config.js` (all colours, shadows, animations defined there)  
- **Radix UI** – primitives for Dialog, Toast, Tabs (if needed), Form controls, etc.  
- **React Hook Form** + **Zod** – form state and validation  
- **Framer Motion** – subtle page transitions  
- **Lucide React** – icons  

No inline styles, no inline hex codes – only Tailwind utility classes and custom utilities from `global.css`.

---

## 🎨 Design System (Utility‑First)

### 1. Tailwind Configuration

Extend `tailwind.config.js` with:

- **Colors** (named tokens):  
  `scryn-bg`, `scryn-primary`, `scryn-primary-light`, `scryn-gold`, `scryn-text-primary`, `scryn-text-secondary`, `scryn-border`, `scryn-success`, `scryn-error`, `scryn-surface`, `scryn-disabled`

- **Spacing & Sizing**: use default Tailwind scale (4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px, 96px)

- **Border radius**:  
  `rounded-sm` (8px) for inputs/buttons  
  `rounded-md` (12px) for cards  
  `rounded-lg` (20px) for hero cards

- **Box shadows** (multi‑layered for cards):  
  Define a custom shadow, e.g., `shadow-premium-card`:  
  - `0 10px 30px -5px rgba(0,0,0,0.05)`  
  - `0 20px 40px -10px rgba(0,0,0,0.1)`  
  - `inset 0 0 0 1px rgba(0,0,0,0.02)`

- **Keyframes & animations**:  
  - `fadeIn`, `slideDown` (200‑300ms)  
  - `shimmer` – for the redeem button (moving gradient)  
  - `spinSlow` – for loading spinners
- And many more.

### 2. Global CSS (`globals.css`)

Only contain:

- Tailwind directives (`@tailwind base; @tailwind components; @tailwind utilities;`)
- A custom utility `.text-gradient-hero` (linear‑gradient from `scryn-primary` to `scryn-gold`, background‑clip text, transparent color)
- Keyframes and animation classes (e.g., `.animate-shimmer`, `.animate-spin-slow`) if not defined in config
- No component‑specific CSS, no inline style blocks

All other styling must use Tailwind utilities.

---

## 🧩 Reusable Components (Extend Radix)

Create a set of **shared components** in `/src/components/ui/` that wrap Radix primitives with Scryn styling (using Tailwind classes). Each component must be fully typed (Props interface, no `any`).

### Required components

| Component | Based on Radix | Description |
|-----------|----------------|-------------|
| `Button` | Radix Slot (optional) | Variants: primary, secondary, ghost, danger. Sizes: sm, md, lg. Support loading state + shimmer variant for redeem button. |
| `Input` | Radix Form primitives | Supports label, error message, success state, icon slots, password toggle. Uses live validation styling. |
| `Card` | None (simple div) | Applies `shadow-premium-card`, rounded corners, padding, background `scryn-surface`. |
| `Toast` | Radix Toast | Position top‑right, auto‑dismiss (4‑6 seconds), types: success, error, info. |
| `Dialog` | Radix Dialog | For modals (email confirmation, password reset, etc.). Includes title, description, actions. |
| `Tabs` | Radix Tabs | Used only if needed (e.g., vendor dashboard – not required for guest pages, but good to have). |
| `Spinner` | None | Simple rotating SVG or div with `border-t-transparent`, coloured with `scryn-primary`. |
| `FormField` | Radix Form | Wraps Input + Label + Error + success icon. Integrates with React Hook Form. |

All components must be **mobile‑first** (full width on mobile, auto on desktop where appropriate), accessible (aria attributes from Radix), and support dark mode? Not needed for v3.

---

## 📄 Page Specifications (No Code, Only Rules)

### 1. Home Page (`/`)

**Layout**  
- Full‑width, centered content, max‑width 1200px, padding consistent.  
- Hero section (60‑70vh minimum) with heading, subheading, two CTAs.  
- Features section (3 columns on desktop, 1 on mobile).  
- Footer with quick links and contact email.

**Hero**  
- Heading: "Redeem Your Reward" – apply `.text-gradient-hero` class.  
- Subheading: friendly copy about scratching a card and getting data.  
- Primary CTA: "Redeem Now →" (large, but not shimmer – that’s only on redemption page).  
- Secondary CTA: "Register Your Business".

**Features** (3 cards)  
- Icon + title + short description.  
- Topics: instant data rewards, works on any phone, safe & simple.

**Footer**  
- Links: Privacy, Terms, Support.  
- Friendly note: "Need help? hello@scryncard.com.ng – we reply fast."

---

### 2. Registration Page (`/register`)

**Layout**  
- Centered card (`shadow-premium-card`) – max width 420px.  
- Heading: "Create your account" (text‑gradient).  
- Subheading: friendly invitation.

**Form fields** (all required, live validation)  
- **Business name** – min 3 chars, max 100. Friendly placeholder example.  
- **Email** – valid format, mock check for existing email on blur. Helper text: "We'll send a confirmation link – check your inbox!"  
- **Phone number** – Nigerian format, auto‑sanitise (strip non‑digits, convert `0` prefix to `234`, display formatted).  
- **Business type** – dropdown (Retail, Telecom, FMCG, Event Organizer, Other).  
- **Password** – show real‑time checklist (8 chars, uppercase, lowercase, number). Toggle visibility.  
- **Confirm password** – must match password.

**Live validation rules**  
- Validate as user types (`onChange` mode).  
- Inline error messages below each field (red, small).  
- Success state: green border + checkmark icon.  
- Submit button disabled until all fields valid.

**Submit button**  
- Label: "Create Account".  
- On click: show spinner, disable form, call mock registration service.  
- On success: open a `Dialog` (modal) with mock email confirmation content (simulated inbox message, fake "Confirm" button). After confirmation, redirect to `/login`.  
- On error: show toast with specific friendly message.

---

### 3. Login Page (`/login`)

**Layout**  
- Centered card (`shadow-premium-card`), max width 420px.  
- Heading: "Welcome back!" (text‑gradient).  
- Subheading: friendly.

**Fields**  
- **Email** – live format validation.  
- **Password** – toggle visibility.

**Forgot password**  
- Link opens a `Dialog` modal: mock password reset (no real email). Friendly message: "We'll send a reset link to your email (mock)."

**Submit**  
- Label: "Sign In".  
- On success: store session token in `localStorage`, show toast "Welcome back, [Business Name]!", redirect to `/dashboard` (vendor area).  
- On error: inline error or toast with friendly message (e.g., "That password doesn't match. Want to reset it?").

**Link to registration**  
- Below form: "Don't have an account? Register here" → `/register`.

---

### 4. Redemption Page (`/redeem`) – Data Only

**Layout**  
- Hero heading: "Redeem Your Card" (text‑gradient).  
- Subheading: friendly instructions.  
- Form card (`shadow-premium-card`), centered, max width 500px.

**Form fields** (live validation + sanitisation)  
- **Serial number** – format `XX-123456` (2 letters, dash, 6 digits). Auto‑uppercase, reject invalid chars. Friendly error: "Example: AB-123456".  
- **Gift code** – 16 lowercase alphanumeric, no spaces/dashes. Auto‑lowercase, strip invalid chars. Type password (masked with toggle).  
- **Phone number** – same sanitisation as registration. Helper text: "We'll detect your network automatically."

**Live validation rules**  
- Each field validates as user types.  
- Submit button enabled only when all three are valid.

**Redeem button**  
- **Size**: large (e.g., 56px height, wide padding).  
- **Background**: `scryn-primary` with **shimmer animation** (defined in `global.css` as a moving linear gradient).  
- **Text**: "Redeem Reward".  
- **States**: default (shimmer), loading (spinner + text "Sending your data..."), disabled.

**Redemption flow (no airtime)**  
1. On submit, call mock redemption service.  
2. Service detects network from phone prefix (mock mapping).  
3. Fetches available data bundles for that network that cost ≤ card value.  
4. Chooses the best bundle (largest data within budget) – or allows selection if multiple (MVP: auto‑pick).  
5. Returns success with bundle name, network, phone number, card value.  

**Success (inline, no page change)**  
- Replace form with success card (same container).  
- Show large green checkmark, "🎉 Reward unlocked!", bundle details (e.g., "MTN 1GB Weekly"), phone number.  
- Friendly message: "It's been sent to your phone. May take a minute."  
- Two buttons: "Download Receipt" (mock PDF), "Redeem Another Card" (resets to form).  

**Error (inline)**  
- Replace form with error card.  
- Show red X, "😕 Something went wrong", specific friendly message (e.g., "Card already used", "Not found", "No data bundles available for your network right now – contact support").  
- Buttons: "Try Again" (reset form), "Go Home".

**No airtime mentions anywhere** – copy, success messages, error messages, service layer all refer only to data bundles.

---

### 5. Success / Error (Inline Only)

No separate routes needed. Both success and error states replace the form content inside the same card container, with smooth transition (fade/scale).

---

## 🧠 Service Layer & Types (Strictly Defined)

### General rules
- All service functions return `Promise<ApiResponse<T>>` where `ApiResponse<T>` is a discriminated union: `{ success: true; data: T } | { success: false; error: string }`.  
- No `any` – every `T` is an explicit interface.  
- Mock implementations simulate network delay (e.g., 1‑2 seconds) and use in‑memory arrays.

### Required services (described, not coded)
- **`authService`**  
  - `register(data: RegisterInput)` – returns business ID, triggers mock email.  
  - `login(email, password)` – returns session token, business details.  
  - `validateSession(token)` – checks expiry, returns session.  
  - `logout(token)` – removes session.

- **`redemptionService`**  
  - `validateAndRedeem(data: RedeemInput)` – returns `RedemptionResult` containing bundle name, network, phone, card value, receipt ID.  
  - Internally uses mock data for cards, campaigns, and network‑to‑bundle mappings.

### Required types (interfaces – describe, don't write)
- `RegisterInput` – business name, email, phone, business type, password, confirmPassword.  
- `LoginInput` – email, password.  
- `RedeemInput` – serialNumber, giftCode, phoneNumber.  
- `RedemptionResult` – rewardType: "data", bundleName, network, phoneNumber, cardValue (number), timestamp, receiptId.  
- `Session` – token, businessId, businessName, email, expiresAt.  
- `ApiResponse<T>` – as above.

All forms have corresponding Zod schemas that infer the TypeScript types (no manual duplication). Fields are validated with `zod` on the client, and errors are mapped to friendly messages.

---

## 🧼 Live Validation & Sanitisation Rules (Describe)

### General
- Validation runs on every keystroke (`onChange`).  
- Each field has a Zod schema that defines valid formats, min/max, regex patterns.  
- Inline error appears immediately when invalid; error disappears when valid.  
- Submit button disabled until all fields are valid and not pristine? (Actually, pristine not required – disabled until all valid after any interaction.)

### Sanitisation (applied on input event before validation)
- **Serial number**: convert to uppercase, strip any character not `A-Z` or `0-9` or dash, then format as `XX-123456` automatically.  
- **Gift code**: convert to lowercase, strip any character not `a-z0-9`, limit to 16 chars.  
- **Phone number**: strip all non‑digits, if starts with `0` replace with `234`, then format as `234-XX-XXX-XXXX` for display (but store raw digits).  
- **Email**: trim whitespace, convert to lowercase.

All sanitised values are written back to the input field (controlled component).

---

## ✨ Friendly Tone Guidelines

- Use **contractions** (you'll, we'll, it's).  
- Emojis: 🎉 (success), 😕 (error), 📱 (mobile), 🔒 (security), ✅ (completion).  
- Error messages: start with "Hmm...", "Oh no...", "Looks like...". Avoid "Invalid", "Error", "Failed" alone.  
- Placeholders: use friendly examples (`e.g., Green House Katsina`).  
- Helper text: conversational (`We'll send a confirmation link – check your inbox!`).  
- Success messages: celebratory (`All done! Your data is on its way.`).  
- Loading text: `Just a moment...`, `Sending your data...`, `Checking your card...`.

---

## ✅ Quality Checklist (For Implementation)

- [ ] No inline hex codes or inline `style` – everything via Tailwind utilities or `global.css`.  
- [ ] All Radix components extended into reusable UI components (`Button`, `Input`, `Card`, `Toast`, `Dialog`, `Tabs`, `Spinner`, `FormField`).  
- [ ] No airtime mentions in copy, types, or mock data.  
- [ ] Hero headings use `.text-gradient-hero`.  
- [ ] Redeem button has large size + shimmer animation (defined in `global.css`).  
- [ ] Multi‑layered card shadow (`shadow-premium-card`) applied to all cards.  
- [ ] Live validation + sanitisation on all forms (register, login, redeem).  
- [ ] Strict TypeScript – every prop, state, service response has explicit interface; no `any`.  
- [ ] Mobile responsive (breakpoints: 640px, 768px, 1024px).  
- [ ] Accessible: labels, focus rings, Radix ensures keyboard navigation.  
- [ ] Session persisted via `localStorage`, validated on protected routes.  
- [ ] Mock services with simulated network delay.  

---

This document is the **final specification** for the guest pages. No code or markup is included – only rules, descriptions, and constraints. The development team will translate this into actual implementation using the defined tech stack and utility‑first methodology.