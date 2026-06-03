# ⚙️ SCRYN v3 — AI BUILD PROMPT (PRODUCTION-READY MVP)

## 🎯 OBJECTIVE

Build a premium, production-ready web application called **Scryn** — a digital scratch card distribution platform for Nigerian businesses.

### What Scryn Does

Scryn enables businesses (retailers, SMEs, event organizers, distributors) to:

- Create branded reward campaigns
- Generate unique scratch cards with secure gift codes
- Distribute cards **offline** to customers
- Allow end users to **redeem rewards online** instantly via phone number
- Track full campaign performance and redemption analytics

### This MVP Scope (v3)

- **Frontend-first implementation** with internal API abstraction layers
- **Mock data services** (no database yet — designed for later MongoDB integration without refactoring)
- **Complete business + redemption flows**
- **Dashboard analytics** for campaign performance
- **Production-ready code quality**

This architecture ensures that UI logic remains independent of backend implementation, allowing seamless transition to real APIs.

---

# 🧱 TECH STACK

### Core Framework

- **Next.js 14+** (App Router) — React framework for production apps
- **TypeScript (strict mode)** — All code must be fully typed, no `any` types
- **React 18+** — Latest React features

### Styling & UI

- **Tailwind CSS** — Utility-first CSS framework (v3+)
- **Radix UI** — Headless component library for accessible primitives
- **Framer Motion** — Production animation library (subtle, performant)
- **Plus Jakarta Sans** — Google Font for premium typography

### State & Validation

- **Zustand** — Lightweight global state (optional, use only if needed)
- **React Hook Form** — Performant form management
- **Zod** — TypeScript-first schema validation library
- **React Router** (optional fallback for client-side routing if App Router insufficient)

### Development & Quality

- **ESLint** — Code consistency & error detection
- **Prettier** (implicit) — Code formatting
- **Next.js built-in** — API routes, middleware, bundling

### Why This Stack

- **Maturity**: All libraries are proven in production
- **Type Safety**: Full TypeScript coverage ensures reliability
- **Performance**: React Server Components + code splitting
- **Developer Experience**: Excellent tooling and documentation
- **Scalability**: Services layer allows mock → real DB migration without UI refactoring

---

# 🏗 ARCHITECTURE PRINCIPLES

## ⚠️ FRONTEND-FIRST API ABSTRACTION LAYER (CRITICAL)

**DO NOT connect directly to any database or external APIs in component/page logic.**

### Rule

All backend/data operations **MUST** go through a service layer. This ensures:

- UI logic remains database-agnostic
- Easy transition from mock services to real APIs
- Testable code
- Single point of change for all API calls

### Service Layer Structure

```
/src
  /services
    auth.service.ts        (login, registration, session)
    campaign.service.ts    (create, list, get, update campaigns)
    card.service.ts        (generate, validate, track cards)
    redemption.service.ts  (process redemption, validate codes)
    analytics.service.ts   (fetch dashboard metrics, charts)
  /lib
    /api
      request.ts           (central mock API handler with delay simulation)
      types.ts             (all request/response types)
    mock-data.ts           (centralized mock database)
```

### How Services Work (Mock Pattern)

Each service method:

1. **Accepts typed parameters** (Zod validated if needed)
2. **Simulates network delay** (500-800ms for realistic UX testing)
3. **Performs mock business logic** (validation, simulation, data transformation)
4. **Returns typed response object** with `success`, `data`, and optional `error`

Example:

```typescript
// services/redemption.service.ts
export const redemptionService = {
  async validateAndRedeem(input: RedeemCodeInput): Promise<ApiResponse<RedemptionResult>> {
    await simulateNetworkDelay();

    // Validate serial number format
    // Validate gift code length
    // Check if already redeemed
    // Simulate processing

    return {
      success: true,
      data: { rewardAmount, expiryDate, ... }
    };
  }
};
```

### Component Usage (CORRECT)

```typescript
// pages/redeem.tsx
"use client";

async function handleRedeem(formData) {
  const result = await redemptionService.validateAndRedeem(formData);
  if (result.success) {
    // Show success
  } else {
    // Show error
  }
}
```

### Component Usage (WRONG - DO NOT DO)

```typescript
// WRONG - Never do this
const result = await db.redemption.create(...);
const response = await fetch('https://external-api.com/redeem', ...);
```

## Feature-Based Folder Structure

```
/src
  /app
    /(auth)
      /login
        page.tsx
        layout.tsx
      /register
        page.tsx
    /(dashboard)
      /campaigns
        page.tsx
        [id]
          page.tsx
      /dashboard
        page.tsx
      layout.tsx
    /(public)
      /redeem
        page.tsx
      layout.tsx
    layout.tsx
    page.tsx
  /components
    /ui                    (primitive reusable components)
      button.tsx
      input.tsx
      card.tsx
      modal.tsx
      toast.tsx
      kpi-card.tsx
      etc.
    /forms                 (feature-specific form components)
      campaign-form.tsx
      redeem-form.tsx
      login-form.tsx
    /layouts
      dashboard-layout.tsx
      auth-layout.tsx
    /shared                (globally used components)
      header.tsx
      sidebar.tsx
      navbar.tsx
  /services
    (service layer - see above)
  /lib
    (shared utilities, types, constants)
  /hooks                   (custom React hooks)
  /stores                  (Zustand store if needed)
  /types                   (global TypeScript types)
  /config                  (environment, constants)
```

---

# 🎨 DESIGN SYSTEM (PREMIUM UI REQUIRED)

## COLOR PALETTE (STRICT - NO EXCEPTIONS)

### Primary Colors

- **Background**: `#FDFFFC` (off-white/cream) — all page backgrounds
- **Primary Action**: `#228B22` (forest green) — buttons, links, CTAs
- **Text Primary**: `#1A1A1A` (near-black) — main text
- **Text Secondary**: `#666666` (medium gray) — secondary text, labels
- **Border**: `#E8E8E8` (light gray) — dividers, input borders
- **Success**: `#10B981` (emerald) — success states, validations
- **Error**: `#EF4444` (red) — error states, alerts
- **Warning**: `#F59E0B` (amber) — warning states
- **Info**: `#3B82F6` (blue) — info states

### Background Layers

- **Surface**: `#FFFFFF` (pure white) — cards, containers
- **Hover**: `#F5F5F5` (light gray) — hover states
- **Disabled**: `#F0F0F0` (pale gray) — disabled elements

**NO additional colors**. All UI must use this palette only.

## VISUAL STYLE GUIDELINES

### Premium Aesthetic

- **Minimalist**: Clean, uncluttered layouts with ample whitespace
- **Modern SaaS**: Inspired by Stripe, Notion, linear.app
- **Glassmorphism**: **Subtle only** — use on backgrounds/modals, NOT primary actions
- **Shadows**: Multi-layered, soft, blurred (never harsh or double shadows)
  - Small: `0 1px 2px 0 rgba(0, 0, 0, 0.05)`
  - Medium: `0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)`
  - Large: `0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)`

### Spacing System (Consistent Throughout)

```
2px, 4px, 8px, 12px, 16px, 24px, 32px, 40px, 48px
```

All margins and padding must use this scale. No arbitrary spacing.

### Typography

- **Font**: Plus Jakarta Sans (Google Fonts)
- **Sizes**: 12px, 14px, 16px, 18px, 20px, 24px, 32px, 40px
- **Weights**: 400 (regular), 500 (medium), 600 (semibold), 700 (bold)
- **Line Height**: 1.5 (body text), 1.4 (headings)

### Animations

- **Framer Motion only** — no CSS animations for complex motion
- **Styles**:
  - Fade-in/out: opacity transitions (200-300ms)
  - Slide transitions: horizontal/vertical movement (300-400ms)
  - Floating blobs: continuous infinite animations in backgrounds
  - **NO aggressive motion**, bouncing, or heavy transitions
  - **Easing**: Use Framer Motion's default `easeInOut` for consistency

### Border Radius (Consistent)

- **Buttons & Inputs**: `8px` (`rounded-lg` in Tailwind)
- **Cards & Containers**: `12px` (`rounded-xl`)
- **Large Components**: `16px` (`rounded-2xl`)

## UI COMPONENT RULES

- **Rounded corners** on every interactive element
- **Consistent padding** inside all containers (16px minimum for desktop, 12px for mobile)
- **High contrast** text on backgrounds (WCAG AA minimum)
- **No color conflicts** — stick to palette only
- **No cluttered layouts** — max 2-3 sections per view
- **Mobile-first responsive** — design for mobile first, scale to desktop
- **No horizontal scrolling** — ever

## Glassmorphism (Use Sparingly)

When used, apply this pattern to backgrounds only:

```css
backdrop-filter: blur(8px);
background-color: rgba(255, 255, 255, 0.8);
border: 1px solid rgba(255, 255, 255, 0.2);
```

---

# 🧩 REUSABLE COMPONENT SYSTEM (CRITICAL)

All components must be fully reusable, responsive, and consistent. Componentize once, use everywhere.

## Primitive Components (UI Foundations)

Location: `/components/ui/`

### Button Component

- **Variants**: `primary` (forest green), `secondary` (gray), `ghost` (transparent), `danger` (red)
- **Sizes**: `sm`, `md`, `lg`
- **States**: Default, hover, active, disabled, loading
- **Loading State**: Shows spinner while `isLoading={true}`
- Must have: proper focus states, disabled cursor, padding consistency

### Input Component

- **Types**: text, email, password, number, tel
- **States**: Default, focused, filled, error, success, disabled
- **Validation States**:
  - Error: red border + error message below
  - Success: green border + checkmark icon
  - Disabled: grayed out, cursor not-allowed
- **Required**: Label, placeholder, helper text, error message
- Must have: `name` attribute for form handling, proper `type` attribute

### Card Component

- **Default Style**: White background, soft shadow (medium), rounded corners
- **Variants**: `default`, `elevated` (larger shadow), `ghost` (no shadow)
- **Responsive**: Padding adjusts mobile (12px) → desktop (20px)
- Uses multi-layer soft shadow
- Optional: header section, footer section

### Modal Component

- **Centering**: Absolutely centered on screen
- **Background**: Blurred backdrop (backdrop-filter: blur(8px))
- **Overlay**: Semi-transparent dark overlay (rgba(0,0,0,0.5))
- **Close**: Click outside or X button closes modal
- **Animation**: Fade-in + slight scale (Framer Motion)
- Must work: on mobile (full-screen with padding), desktop (centered box)

### Toast/Notification System

- **Types**: `success`, `error`, `info`, `warning`
- **Duration**: Auto-dismiss after 4 seconds (user can close manually)
- **Position**: Top-right corner
- **Animation**: Slide-in from right, fade-out
- **Icon**: Appropriate icon per type (checkmark, X, info, warning)
- Multiple toasts: stack vertically

### KPI Card Component

- **Use Case**: Dashboard metric display
- **Structure**:
  - Metric label (small, gray text)
  - Large number value
  - Optional trend indicator (up/down arrow with percent)
  - Optional sparkline chart
- **Responsive**: Stack vertically on mobile, grid on desktop
- **Styling**: Soft shadow, rounded, white background, hover effect

### Form Component (React Hook Form Wrapper)

- **Structure**: Wraps form elements with validation
- **Features**: Real-time validation, error display, success feedback
- **Integration**: Works with Zod for schema validation
- **Must Include**: Field-level error messages, submit button state

### Table Component

- **Responsive**: Horizontal scroll on mobile (with proper UX), full width on desktop
- **Sortable**: Click headers to sort (up/down indicators)
- **Pagination**: Built-in pagination controls
- **Empty State**: Shows "No data" message with illustration
- **Loading**: Shows skeleton rows while loading
- **Striped Rows**: Alternating row colors for readability

## Component Requirements (ALL COMPONENTS)

- ✅ **Fully typed** with TypeScript (no `any`)
- ✅ **Responsive** (mobile-first approach)
- ✅ **Accessible** (semantic HTML, proper labels, ARIA attributes)
- ✅ **Keyboard navigable** (focus states visible, Tab/Enter support)
- ✅ **Consistent styling** (uses design system only)
- ✅ **No hardcoded colors** (use Tailwind CSS variables from config)
- ✅ **Documented** (brief JSDoc comments for props)
- ✅ **No duplicate logic** (reuse across features)

---

# 🔐 CORE FEATURES (MVP SCOPE)

## 1. BUSINESS SYSTEM & ONBOARDING

### Registration Flow

- **Page**: `/register`
- **Fields**:
  - Business Name (required)
  - Email (required, email validation)
  - Password (required, min 8 chars, include uppercase/lowercase/number)
  - Phone Number (required, Nigeria format: 234...)
  - Business Type (dropdown: Retail, Telecom, FMCG, Event, Other)
- **Validation**: Real-time, per-field feedback
- **Success**: Redirect to login page with confirmation toast
- **Error**: Show inline field errors

### Login Flow

- **Page**: `/login`
- **Fields**: Email, Password
- **Validation**: Format check (real-time), credential validation (on submit)
- **Session**: Store session in service layer (mock for now)
- **Success**: Redirect to `/dashboard`
- **Error States**:
  - Invalid email format
  - Account not found
  - Incorrect password
  - Account not yet approved

### Session/Auth Service

- **Mock behavior**: Simulate approval delay (business status = "pending" initially, auto-approve after 2 seconds for demo)
- **Session persistence**: Store in localStorage (with expiry simulation)
- **Auto-logout**: After 30 minutes of inactivity (simulated)
- **Types to create**: `Business`, `Session`, `AuthResponse`

## 2. CAMPAIGN SYSTEM

### Create Campaign Flow

- **Page**: `/dashboard/campaigns/new`
- **Multi-step form OR single form with sections**:

  **Step 1: Campaign Details**
  - Campaign Name (required, string)
  - Description (optional, text)
  - Reward Type (dropdown: Airtime, Data, Value Credit)
  - Status (auto-set to "active" on creation)

  **Step 2: Card Configuration**
  - Total Cards Quantity (required, number > 0)
  - Denominations (varies by reward type):
    - **Airtime**: ₦200, ₦500, ₦1000, ₦2000, ₦5000
    - **Data**: 1GB, 2GB, 5GB, 10GB
    - **Value Credit**: ₦100-₦5000 (input field)
  - Quantity per denomination (input for each)
  - Sum validation: Total must equal Quantity

  **Step 3: Review & Create**
  - Show summary of campaign
  - Button to create campaign

### Campaign List/Overview

- **Page**: `/dashboard/campaigns`
- **Display**: Table or card grid
- **Columns/Info**: Campaign name, reward type, total cards, status, created date, redemption count
- **Actions**: View details, edit (if pending), delete (if no redeemed cards)
- **Pagination**: 10 items per page with Next/Previous buttons
- **Empty State**: "No campaigns yet. Create your first campaign." with CTA button
- **Filter/Sort**: Filter by status (active, completed), sort by date/name

### Campaign Details Page

- **Page**: `/dashboard/campaigns/[id]`
- **Display**:
  - Campaign overview (name, type, total cards, status)
  - Card breakdown by denomination (visual chart)
  - Redemption stats (total redeemed, success rate, recent redemptions table)
  - Action buttons: View cards, Download report, Export data
  - Edit button (if applicable)

## 3. SCRATCH CARD ENGINE (MOCK LOGIC)

### Card Generation Algorithm (Internal)

When a campaign is created, automatically generate all scratch cards:

```
For each denomination in campaign:
  For count = 1 to quantity:
    serialNumber = generateSerial()        // Format: AB-123456 (alphanumeric)
    giftCode = generateGiftCode()          // Format: 16-char hex hash
    checksum = generateChecksum(serial)    // For validation
    cardData = {
      id: uuid(),
      serialNumber,
      giftCode,
      checksum,
      campaignId,
      denomination,
      status: 'active',
      createdAt
    }
    store in mock database
```

### Card Generation Functions

**serialNumber**: 2 uppercase letters + 6 digits (e.g., `AB-123456`)
**giftCode**: 16 lowercase hex characters (e.g., `a1b2c3d4e5f6g7h8`)
**checksum**: XOR of all characters for basic validation

**DO NOT expose generation logic in UI** — only in `/services/card.service.ts`

## 4. REDEMPTION SYSTEM (CRITICAL FEATURE)

### Public Redemption Page

- **Route**: `/redeem` (public, no authentication)
- **Page Title**: "Redeem Your Reward" or "Scratch & Win"
- **Hero Section**: Brief explanation of process

### Redemption Form

**Fields** (all required):

1. **Scratch Card Serial Number**
   - Placeholder: "e.g., AB-123456"
   - Max length: 9 characters
2. **Gift Code**
   - Placeholder: "e.g., a1b2c3d4e5f6g7h8"
   - Max length: 16 characters
   - Input type: password (hide by default, show toggle)
3. **Phone Number**
   - Placeholder: "e.g., 2348012345678"
   - Accept Nigeria format only (start with 234 or 0)
   - Auto-format to 11 digits

### Real-Time Validation (AS USER TYPES)

**Serial Number Validation**:

- Format: `^[A-Z]{2}-\d{6}$` (2 letters, dash, 6 digits)
- Success state: Green border + checkmark icon
- Error state: Red border + error message "Invalid format"
- Empty: Gray border

**Gift Code Validation**:

- Format: `^[a-z0-9]{16}$` (exactly 16 lowercase hex chars)
- Success state: Green border + checkmark
- Error state: Red border + error message "Invalid code format"

**Phone Number Validation**:

- Nigeria format: Must start with 234 or 0, contain exactly 11 digits
- Auto-format: Strip spaces/dashes, prepend 234 if starts with 0
- Success state: Green border + formatted display "234-80-1234-5678"
- Error state: Red border + error message "Invalid Nigerian phone"

### Submit Button Logic

- **Disabled** until ALL fields are valid (green states)
- **Show spinner** while validating
- **Never** allow submit with invalid fields

### Validation Response Flow

```
1. User enters serial + code + phone
2. All fields real-time validate
3. Button becomes enabled (when all green)
4. User clicks submit
5. Service calls redemptionService.validateAndRedeem(input)
6. Show loading spinner on button
7. Service simulates network delay + validation checks:
   - Serial/code exists in database
   - Card not already redeemed
   - Phone number format valid
   - Reward still available
8. Return success or error response
```

### Success Screen

- **Show after successful redemption**:
  - ✅ "Redemption Successful!"
  - Reward details (amount, type, network)
  - Message: "Your ₦500 airtime has been credited to 08012345678"
  - Timestamp of redemption
  - Receipt button (download/print)
  - "Redeem Another" button (reset form)

### Failure Screen

- **Show after failed redemption**:
  - ❌ Error message (specific reason)
  - Options:
    - "Check Details" (pre-fill form, let user retry)
    - "Contact Support" (show support email/phone)
    - "Go Home" (link to home page)

### Common Error Cases (Handle All)

1. "Serial number not found" — Card doesn't exist
2. "This card has already been redeemed" — Cross check serial + code in DB
3. "Invalid phone number" — Must be Nigeria format
4. "Reward expired" — Campaign ended
5. "Network error" — Simulated API timeout

## 5. BUSINESS DASHBOARD

### Dashboard Home Page

- **Route**: `/dashboard`
- **Authentication**: Protected (require login)
- **Welcome Message**: "Welcome back, [Business Name]"

### KPI Section (Top of Page)

Display 4 key metrics in KPI cards:

1. **Total Cards Issued**: Number + % vs last month
2. **Total Redemptions**: Number + % success rate
3. **Redemption Rate**: Percentage with trend indicator
4. **Revenue Generated**: ₦ amount (optional for MVP)

### Active Campaigns Section

- **Widget**: Campaign overview
- **Display**:
  - Number of active campaigns
  - Number of pending campaigns
  - Quick links to view all
- **Cards per campaign**: Name, type, progress bar (redeemed/total), status badge

### Redemption Analytics Chart

- **Chart Type**: Line chart (Recharts)
- **X-axis**: Last 7 days
- **Y-axis**: Redemptions per day
- **Tooltip**: Show count on hover
- **Legend**: Redemptions, Target (optional)
- **Responsive**: Full width on mobile, fixed aspect ratio on desktop

### Recent Redemptions Table

- **Display**: Last 5 recent redemptions
- **Columns**: Phone Number (masked: **\***5678), Campaign, Reward, Status, Timestamp
- **Sortable**: Click column headers
- **Pagination**: Link to "View All Redemptions" page
- **Empty State**: "No redemptions yet"

### Sidebar/Navigation

- **Dashboard**: Home
- **Campaigns**: List all campaigns, create new
- **Redemptions**: View all redemption logs, export data
- **Settings**: Profile, business details
- **Logout**: Sign out

---

# 🧠 INTERNAL API LAYER (MOCK SERVICES - PRODUCTION PATTERN)

**All data operations go through service layer only. No direct database queries in components.**

## Service Layer Structure

```typescript
// /src/services/auth.service.ts
export const authService = {
  async register(input: RegisterInput): Promise<ApiResponse<Business>> {
    // Simulate network delay
    // Validate input with Zod
    // Generate mock business record
    // Store in mock database
    // Return success or error
  },

  async login(email: string, password: string): Promise<ApiResponse<Session>> {
    // Validate credentials against mock database
    // Generate session token
    // Return session or error
  },

  async validateSession(token: string): Promise<ApiResponse<Session>> {
    // Check if token is valid and not expired
    // Return session or error
  },
};

// /src/services/campaign.service.ts
export const campaignService = {
  async createCampaign(
    input: CreateCampaignInput,
  ): Promise<ApiResponse<Campaign>> {
    // Validate campaign data
    // Auto-generate scratch cards
    // Store campaign + cards in mock DB
    // Return campaign ID
  },

  async listCampaigns(businessId: string): Promise<ApiResponse<Campaign[]>> {
    // Fetch all campaigns for business
    // Include redemption stats
  },

  async getCampaignDetails(
    campaignId: string,
  ): Promise<ApiResponse<CampaignWithStats>> {
    // Fetch campaign + detailed stats
  },
};

// /src/services/redemption.service.ts
export const redemptionService = {
  async validateAndRedeem(
    input: RedeemInput,
  ): Promise<ApiResponse<RedemptionResult>> {
    // Validate serial number format
    // Validate gift code format
    // Validate phone number format
    // Check if card exists
    // Check if already redeemed
    // Process redemption
    // Return result
  },

  async getRedemptionHistory(
    campaignId: string,
  ): Promise<ApiResponse<Redemption[]>> {
    // Fetch all redemptions for campaign
  },
};

// /src/lib/api/request.ts (Central Mock Handler)
async function mockApiCall<T>(
  operation: () => Promise<T>,
  options?: { delay?: number },
): Promise<T> {
  const delay = options?.delay || 500;
  await new Promise((resolve) => setTimeout(resolve, delay));
  return operation();
}

// /src/lib/mock-data.ts (Mock Database)
export const mockDatabase = {
  businesses: [],
  campaigns: [],
  cards: [],
  redemptions: [],
  sessions: [],
};
```

## Service Response Types (All Services Use This)

```typescript
// /src/lib/api/types.ts
export interface ApiResponse<T> {
  success: boolean;
  data?: T;
  error?: string;
  timestamp?: number;
}

export interface PaginatedResponse<T> {
  success: boolean;
  data: T[];
  pagination: {
    page: number;
    limit: number;
    total: number;
    pages: number;
  };
}

export interface ValidationError {
  field: string;
  message: string;
}

export interface ApiErrorResponse {
  success: false;
  error: string;
  validationErrors?: ValidationError[];
}
```

## Key Rules for Services

1. **Always simulate network delay** (500-800ms)
   - Creates realistic UX testing experience
   - Ensures UI handles loading states properly

2. **Validate all inputs** (use Zod)
   - Don't trust client-side validation alone
   - Return specific error messages

3. **Always return typed responses**
   - Never return raw data
   - Always include `success` flag
   - Include `error` message on failure

4. **Simulate real-world scenarios**
   - Duplicate detection (duplicate email in register)
   - Not found errors (campaign doesn't exist)
   - Already redeemed cards
   - Expired campaigns/rewards

5. **Store all data in mock database** (not localStorage)
   - Use in-memory object or simple file-based mock
   - Persist across page navigations (simulation)
   - Clear on app reload (or use IndexedDB if needed)

---

# 🧾 DATA MODELS (TYPESCRIPT TYPES ONLY - NO DATABASE YET)

Create all types in `/src/lib/types/` or `/src/types/` directory.

## Business Type

```typescript
export interface Business {
  id: string; // UUID
  name: string;
  email: string;
  passwordHash?: string; // Never send to client
  phone: string; // Nigeria format (234...)
  businessType: "retail" | "telecom" | "fmcg" | "event" | "other";
  status: "pending" | "active" | "suspended";
  createdAt: Date;
  updatedAt: Date;
  totalCampaigns: number; // Computed
  totalRedemptions: number; // Computed
}
```

## Campaign Type

```typescript
export interface Campaign {
  id: string;
  businessId: string;
  name: string;
  description?: string;
  rewardType: "airtime" | "data" | "value_credit";
  status: "active" | "pending" | "completed" | "cancelled";
  totalCards: number;
  redeemableCards: number; // totalCards - redeemed count
  denominations: Denomination[];
  createdAt: Date;
  updatedAt: Date;
  startDate?: Date;
  endDate?: Date;
  metadata?: Record<string, unknown>;
}

export interface Denomination {
  value: number | string; // 500 (airtime), '5GB' (data)
  quantity: number;
  redeemed: number;
}
```

## ScratchCard Type

```typescript
export interface ScratchCard {
  id: string;
  campaignId: string;
  serialNumber: string; // Format: AB-123456
  giftCode: string; // 16-char hex
  checksum: string; // For validation
  denomination: number | string;
  status: "active" | "redeemed" | "expired" | "fraud";
  redeemedBy?: string; // Phone number (masked)
  redeemedAt?: Date;
  createdAt: Date;
  expiryDate?: Date;
}
```

## Redemption Type

```typescript
export interface Redemption {
  id: string;
  cardId: string;
  campaignId: string;
  phoneNumber: string; // Format: 234...
  status: "success" | "failed" | "pending";
  rewardValue: string | number;
  rewardType: "airtime" | "data" | "value_credit";
  failureReason?: string; // If status === 'failed'
  createdAt: Date;
  processedAt?: Date;
}

export interface RedemptionStats {
  totalRedemptions: number;
  successfulRedemptions: number;
  failedRedemptions: number;
  redemptionRate: number; // Percentage
  revenueGenerated: number; // Optional
}
```

## Session Type

```typescript
export interface Session {
  id: string;
  businessId: string;
  token: string; // JWT-like (can be simple string in mock)
  expiresAt: Date;
  createdAt: Date;
}
```

## Form Input Types (Validation)

```typescript
export interface RegisterInput {
  name: string;
  email: string;
  password: string;
  phone: string;
  businessType: string;
}

export interface LoginInput {
  email: string;
  password: string;
}

export interface CreateCampaignInput {
  name: string;
  description?: string;
  rewardType: "airtime" | "data" | "value_credit";
  denominations: Array<{ value: string | number; quantity: number }>;
}

export interface RedeemInput {
  serialNumber: string;
  giftCode: string;
  phoneNumber: string;
}
```

---

# ⚡ UX/INTERACTION RULES (STRICT IMPLEMENTATION)

## Required States for Every Feature

### Loading States

- Show spinner/skeleton while fetching data
- Button shows spinner while processing
- Disable interactions while loading
- Toast: "Loading..." (if operation takes > 1 second)

### Empty States

- Never show blank page
- Show relevant icon + message + CTA button
- Examples:
  - "No campaigns yet. Create your first campaign" → CTA button
  - "No redemptions yet" → Link to redemption page
  - Empty table → "No data to display"

### Error States

- **Form field errors**: Inline error message below input (red text, red border)
- **API errors**: Toast notification (red background, 5 second duration)
- **Page-level errors**: Full error card with retry button
- **Validation errors**: Real-time feedback per field
- Always provide user action: "Retry", "Go back", "Contact support"

### Success States

- **Form submission**: Toast notification with checkmark icon
- **Validation fields**: Green border + checkmark icon
- **Completed action**: Success screen or toast notification
- **Message**: Clear, positive language ("Added successfully", "Saved!")

## Form Behavior

### Real-Time Validation

- Validate as user types (not just on blur or submit)
- Show error/success icon immediately
- Update button state based on form validity
- No submit unless form valid

### Inline Feedback

- Error message appears below field (red, 12px)
- Success state: green border + checkmark
- Helper text: gray, 12px, above input
- Character count (if applicable): right-aligned, 12px

### Submit Button Logic

- **Disabled state**: When form has errors OR is submitting
- **Loading state**: Show spinner, disable all form inputs
- **Success state**: Navigate away or show success screen
- **Error state**: Show error toast, keep form state, allow retry

## Toast Notifications

- **Position**: Top-right corner
- **Duration**: 4 seconds auto-dismiss (unless error, then 6 seconds)
- **Content**: Icon + message + close button (optional)
- **Multiple**: Stack vertically with 8px gap
- **Types**: success (green), error (red), info (blue), warning (amber)

## Navigation & Flow

- **Breadcrumbs**: Show on all pages except home/login
- **Back button**: Always available (browser back or custom button)
- **Redirect after action**:
  - Register → Login page
  - Login → Dashboard
  - Create campaign → Campaign details or dashboard
  - Redeem successfully → Success screen
- **Prevent accidental loss**:
  - Warn if leaving unsaved form
  - Confirm destructive actions (delete)

## Accessibility Requirements

- **Keyboard navigation**: Tab through all focusable elements in logical order
- **Focus indicators**: Visible, 2px outline, blue/green color
- **Semantic HTML**: Use `<button>`, `<input>`, `<form>`, `<table>` properly
- **Labels**: All inputs have `<label>` with `htmlFor` attribute
- **ARIA attributes**: `aria-label`, `aria-describedby` where needed
- **Color contrast**: Text must meet WCAG AA standard (4.5:1 for normal text)
- **Focus trap in modals**: Tab stays within modal, trap at top/bottom
- **Screen reader support**: All images have alt text, form errors announced

## Motion & Animation

- **Page transitions**: Fade in (200ms)
- **Form validation**: Icon fade-in (150ms)
- **Modal appearance**: Scale-up + fade (300ms)
- **Hover effects**: Subtle color shift, cursor change
- \*\*Loading: Spinner animation (continuous 1.5s rotation)
- **No motion**: Respect `prefers-reduced-motion` media query

---

# 📱 RESPONSIVE DESIGN (MOBILE-FIRST)

## Breakpoints

- **Mobile**: 320px - 640px (default/base styles)
- **Tablet**: 640px - 1024px (md breakpoints)
- **Desktop**: 1024px+ (lg/xl breakpoints)

## Rules

- **Mobile-first approach**: Design for mobile first, progressively enhance for larger screens
- **No horizontal scrolling**: Ever
- **Touch targets**: Minimum 44px × 44px for buttons/inputs
- **Responsive typography**: Headings scale, body text readable at all sizes
- **Responsive images**: Use CSS `max-width: 100%`
- **Flexible layouts**: Use CSS Grid/Flexbox, not fixed widths
- **Viewport meta**: `<meta name="viewport" content="width=device-width, initial-scale=1" />`

## Mobile-Specific Patterns

- **Sidebar**: Hamburger menu on mobile, full sidebar on desktop
- **Tables**: Stack columns on mobile, show all columns on desktop
- **Modals**: Full-screen with padding on mobile, centered box on desktop
- **Forms**: Single column on mobile, multi-column on desktop
- **Grid layouts**: 1 column mobile, 2-3 columns tablet, 3-4 columns desktop

---

# ♿ ACCESSIBILITY (WCAG 2.1 AA MINIMUM)

- **Semantic HTML**: Proper heading hierarchy, landmarks (`<nav>`, `<main>`, `<form>`)
- **Form labels**: All inputs must have associated labels
- **Focus management**: Visible focus indicator on all interactive elements
- **ARIA attributes**: Use where semantic HTML insufficient
- **Color**: Never rely on color alone to convey information
- **Text alternatives**: Images must have alt text
- **Keyboard**: All functionality accessible via keyboard
- **Motion**: Respect `prefers-reduced-motion`
- **Error messages**: Clear, specific, associated with form field
- **Language**: `<html lang="en">` or appropriate language code

---

# 🚫 HARD CONSTRAINTS (CRITICAL)

✗ NO backend database integration (yet)
✗ NO direct MongoDB/Prisma usage in components
✗ NO inconsistent UI styling or color palette violations
✗ NO hardcoded mock logic inside UI components (must be in services)
✗ NO `any` types in TypeScript (strict mode)
✗ NO unstructured API response types
✗ NO duplicate components (reuse always)
✗ NO heavy animations that ignore `prefers-reduced-motion`
✗ NO form validation only on submit (must be real-time)
✗ NO disabled buttons without clear reason
✗ NO loading states without spinner/skeleton
✗ NO error states without helpful message

---

# 🧭 PRODUCT POSITIONING

**Scryn is:**

> A premium digital scratch card infrastructure system for offline-to-online customer engagement and reward distribution in Nigeria.

**Scryn is NOT:**

- A fintech system or payment processor
- A telecom service provider
- A gambling platform
- A social media app

---

# � CODING STANDARDS & BEST PRACTICES

## TypeScript (Strict Mode)

- **No `any` types**: Every variable, parameter, and return type must be explicitly typed
- **Use generics**: For reusable functions/components (e.g., `async function<T>`)
- **Enums**: Use for fixed set of values (`RewardType`, `CampaignStatus`)
- **Type files**: Keep all types in dedicated `/src/types/` or `/src/lib/types/`
- **Export types**: Export all types that are used across files

## File Organization

- **One component per file** (except tiny utils)
- **Clear naming**: `UserForm.tsx`, `campaign.service.ts`, `validatePhone.ts`
- **Consistent structure**:
  ```
  /components
    /ui                 (primitive reusable components)
    /forms              (form components)
    /layouts            (page layouts)
    /shared             (globally used components)
  /services             (business logic, API calls)
  /lib                  (utilities, constants, types)
  /hooks                (custom React hooks)
  /stores               (Zustand state if needed)
  /types                (global types)
  /app                  (Next.js pages/routes)
  ```

## Component Patterns

```typescript
// ✅ CORRECT: Typed component with props
interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  disabled?: boolean;
  onClick?: () => void;
  children: React.ReactNode;
}

export const Button: React.FC<ButtonProps> = ({
  variant = 'primary',
  size = 'md',
  disabled,
  onClick,
  children
}) => {
  return (
    <button
      className={cn(buttonVariants({ variant, size }))}
      disabled={disabled}
      onClick={onClick}
    >
      {children}
    </button>
  );
};
```

## Service Pattern

```typescript
// ✅ CORRECT: Service with typed responses
export const campaignService = {
  async createCampaign(
    input: CreateCampaignInput,
  ): Promise<ApiResponse<Campaign>> {
    await simulateNetworkDelay();

    // Validation
    // Business logic
    // Return typed response

    return {
      success: true,
      data: campaign,
    };
  },
};
```

## Form Validation Pattern

```typescript
// Use React Hook Form + Zod
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';

const schema = z.object({
  email: z.string().email('Invalid email'),
  password: z.string().min(8, 'Min 8 characters')
});

type FormData = z.infer<typeof schema>;

export const LoginForm = () => {
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting }
  } = useForm<FormData>({
    resolver: zodResolver(schema)
  });

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      {/* Form fields */}
    </form>
  );
};
```

## Hook Pattern (Custom Hooks)

```typescript
// ✅ Custom hook for shared logic
export const usePagination = (items: any[], itemsPerPage: number) => {
  const [currentPage, setCurrentPage] = useState(1);

  const paginatedItems = items.slice(
    (currentPage - 1) * itemsPerPage,
    currentPage * itemsPerPage,
  );

  return { paginatedItems, currentPage, setCurrentPage };
};
```

## Code Quality

- **DRY (Don't Repeat Yourself)**: Reuse components, hooks, utilities
- **SOLID principles**: Single responsibility, open/closed, etc.
- **Error handling**: Always catch and handle errors gracefully
- **Comments**: Explain WHY, not WHAT (code should be self-explanatory)
- **Naming**: Use descriptive names (no `x`, `temp`, `data2`)
- **Constants**: Extract magic strings/numbers to constants at top of file

## Git & Commits

- **Commits**: Small, logical, descriptive messages
- **Branch naming**: `feature/campaign-creation`, `fix/validation-bug`
- **Code review**: Ensure quality before merging

## Testing (Optional, but Recommended)

- **Unit tests**: For services, utils, validators
- **Component tests**: For complex UI logic
- **E2E tests**: For critical user flows (login, redeem)
- **Framework**: Jest, React Testing Library, Playwright

## Performance Best Practices

- **Code splitting**: Use dynamic imports for large components
- **Image optimization**: Use `next/image` component
- **Lazy loading**: Lazy load routes and heavy components
- **Memoization**: Use `React.memo` and `useMemo` carefully (profile first)
- **Bundle size**: Avoid large dependencies, tree-shake when possible

---

# 🚀 DELIVERABLES & OUTPUT EXPECTATIONS

Generate:

1. **Full Next.js App Router Project Structure**
   - All folders organized as per architecture
   - Entry point: `app/page.tsx` (home)
   - App router directory structure (`(auth)`, `(dashboard)`, `(public)`)

2. **Service Layer** (Zero Database - Mock Only)
   - `src/services/auth.service.ts`
   - `src/services/campaign.service.ts`
   - `src/services/card.service.ts`
   - `src/services/redemption.service.ts`
   - `src/services/analytics.service.ts`
   - `src/lib/api/types.ts` + `request.ts`
   - `src/lib/mock-data.ts` (centralized mock database)

3. **Complete Component System** (Reusable, Responsive, Accessible)
   - Primitive UI components (Button, Input, Card, Modal, Toast, KPI, Table, etc.)
   - Form components (LoginForm, RegisterForm, CampaignForm, RedeemForm)
   - Layout components (DashboardLayout, AuthLayout, etc.)
   - Page components (all routes fully functional)

4. **All Feature Pages** (Production-Ready)
   - `/` (home page)
   - `/register` (business registration)
   - `/login` (business login)
   - `/dashboard` (main dashboard with KPIs, charts, recent redemptions)
   - `/dashboard/campaigns` (list, create, view details)
   - `/dashboard/campaigns/[id]` (campaign details + analytics)
   - `/redeem` (public redemption page with real-time validation)
   - `/success` (redemption success)
   - `/error` (error handling)

5. **Type System** (Full TypeScript Coverage)
   - `src/types/` folder with all domain models
   - `src/types/api.ts` (API response types)
   - `src/types/forms.ts` (form input types)
   - `src/types/models.ts` (domain models)
   - No `any` types anywhere

6. **Design System Implementation**
   - Tailwind CSS configuration with defined color palette
   - Custom color variables in `tailwind.config.ts`
   - Global styles with soft shadows, spacing system
   - Responsive typography scale
   - Animation utilities using Framer Motion

7. **State Management** (Optional, if needed)
   - Zustand store for session/auth (if needed)
   - Or React Context for session
   - Keep minimal - prefer local state

8. **Code Quality**
   - ESLint configured
   - TypeScript strict mode enabled
   - All files type-safe
   - No console errors/warnings
   - Consistent code style

9. **Mock Data**
   - Realistic business, campaign, card, redemption data
   - Sufficient data for dashboard pagination/sorting
   - Date generation realistic (past dates for historical data)

10. **README** (Brief)
    - Tech stack summary
    - How to run (`npm install`, `npm run dev`)
    - Project structure overview
    - Service layer explanation
    - How to test different features

---
