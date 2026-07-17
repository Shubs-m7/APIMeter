# Design System Specification - APIMeter

**Project:** APIMeter
**Tagline:** Secure API Key Management & Real-Time Usage Analytics Platform
**Version:** 1.0

This document defines the strict visual language and UI architecture for APIMeter. It acts as the single source of truth for all aesthetics, component behaviors, design tokens, and motion guidelines.

---

## SECTION 1 — Design Philosophy

Our design system is heavily inspired by the brutalist, highly functional, and extremely premium developer aesthetics seen in Vercel, Stripe, Linear, and Supabase.

*   **Consistency:** Predictability breeds trust. A button in settings must look and behave exactly like a button in the project dashboard.
*   **Hierarchy:** Users should instantly know where to look. Data (like API Keys and Logs) is the hero; chrome is secondary.
*   **Whitespace:** Let the interface breathe. Dense data tables are fine, but the surrounding layout requires ample negative space to reduce cognitive load.
*   **Motion:** Animations must be purposeful, subtle, and lightning-fast. Never delay a user's action for the sake of an animation.
*   **Feedback:** Every interaction (hover, click, error, success) requires immediate and unambiguous visual feedback.
*   **Clarity:** Use high-contrast colors and legible typography. Avoid jargon in UI copy.
*   **Accessibility:** An inaccessible app is a broken app. We target WCAG AA compliance strictly.

---

## SECTION 2 — Design Tokens

Design tokens are the foundational building blocks of our UI. They abstract hardcoded values into semantic variables (e.g., `--color-primary` instead of `#2563EB`).

| Token Category | Usage | Tailwind Prefix | Example Variable |
| :--- | :--- | :--- | :--- |
| **Colors** | Backgrounds, text, borders | `bg-`, `text-`, `border-` | `--background` |
| **Typography** | Font families, sizes, weights| `font-`, `text-`, `leading-`| `--font-sans` |
| **Spacing** | Margins, paddings, gaps | `m-`, `p-`, `gap-` | `var(--spacing-4)` |
| **Radius** | Border radii for components | `rounded-` | `--radius` |
| **Borders** | Stroke widths | `border-` | `1px` (hardcoded usually) |
| **Shadows** | Elevations, focus rings | `shadow-` | `--shadow-sm` |
| **Opacity** | Disabled states, overlays | `opacity-` | `0.5` |
| **Z-Index** | Stacking contexts | `z-` | `z-50` (Modals) |
| **Transitions** | Easing functions | `ease-` | `ease-out` |
| **Animation Durations**| Timing | `duration-` | `150ms` |
| **Breakpoints** | Responsive design boundaries | `md:`, `lg:` | `1024px` |

---

## SECTION 3 — Color System

APIMeter is **Dark-First**. The primary aesthetic utilizes the "Zinc" (cool gray) palette with vibrant Indigo accents for interactive elements.

| Role | Token Variable | Dark Mode Value (Zinc) | Light Mode Value (Zinc) | Usage |
| :--- | :--- | :--- | :--- | :--- |
| **Primary** | `--primary` | `#fafafa` (zinc-50) | `#18181b` (zinc-900) | Primary buttons, active states. |
| **Primary Fg** | `--primary-foreground`| `#18181b` (zinc-900) | `#fafafa` (zinc-50) | Text inside primary components. |
| **Secondary** | `--secondary` | `#27272a` (zinc-800) | `#f4f4f5` (zinc-100) | Secondary buttons, subtle fills. |
| **Secondary Fg**| `--secondary-foreground`| `#fafafa` (zinc-50) | `#18181b` (zinc-900) | Text inside secondary components. |
| **Accent** | `--accent` | `#6366f1` (indigo-500) | `#4f46e5` (indigo-600) | Links, focus rings, callouts. |
| **Success** | `--success` | `#22c55e` (green-500) | `#16a34a` (green-600) | Success toasts, 200 OK statuses. |
| **Warning** | `--warning` | `#f59e0b` (amber-500) | `#d97706` (amber-600) | Warning badges, rate limits. |
| **Danger** | `--destructive` | `#ef4444` (red-500) | `#dc2626` (red-600) | Delete buttons, error states. |
| **Background**| `--background` | `#09090b` (zinc-950) | `#ffffff` (white) | App background. |
| **Surface** | `--card` | `#18181b` (zinc-900) | `#ffffff` (white) | Cards, modals, popovers. |
| **Border** | `--border` | `#27272a` (zinc-800) | `#e4e4e7` (zinc-200) | Input borders, dividers. |
| **Muted Text**| `--muted-foreground` | `#a1a1aa` (zinc-400) | `#71717a` (zinc-500) | Helper text, disabled text. |
| **Main Text** | `--foreground` | `#fafafa` (zinc-50) | `#09090b` (zinc-950) | Primary body text. |

---

## SECTION 4 — Typography

Our typography creates a stark contrast between standard UI text and technical data.

*   **Primary Font (`--font-sans`):** `Inter`. Used for all general UI, headings, buttons, and paragraphs.
*   **Code Font (`--font-mono`):** `JetBrains Mono`. Used exclusively for API Keys, UUIDs, Request IDs, and code blocks.

| Level | Tailwind Class | Size / Line-Height | Weight | Usage |
| :--- | :--- | :--- | :--- | :--- |
| **H1** | `text-4xl tracking-tight` | 36px / 40px | Bold (700) | Page titles. |
| **H2** | `text-3xl tracking-tight` | 30px / 36px | SemiBold (600) | Section titles. |
| **H3** | `text-2xl tracking-tight` | 24px / 32px | SemiBold (600) | Modal titles, Card titles. |
| **Body (Lg)**| `text-lg leading-relaxed`| 18px / 28px | Normal (400) | Large introductory text. |
| **Body (Base)**| `text-base` | 16px / 24px | Normal (400) | Standard paragraphs. |
| **Body (Sm)** | `text-sm` | 14px / 20px | Medium (500) | Table data, form labels. |
| **Caption** | `text-xs text-muted-foreground` | 12px / 16px | Normal (400) | Timestamps, extremely fine print. |
| **Button Text**| `text-sm font-medium` | 14px / 20px | Medium (500) | All interactive buttons. |
| **Code** | `font-mono text-sm` | 14px / 20px | Normal (400) | API Keys (`apim_12345...`). |

---

## SECTION 5 — Spacing System

We use a strict **8px baseline grid** (sub-divided into 4px for micro-adjustments).

| Token | Pixels | Rem | Tailwind | Usage |
| :--- | :--- | :--- | :--- | :--- |
| `spacing-1` | 4px | 0.25rem | `p-1`, `gap-1` | Micro gaps between icons and text. |
| `spacing-2` | 8px | 0.5rem | `p-2`, `gap-2` | Small paddings inside inputs/buttons. |
| `spacing-4` | 16px | 1rem | `p-4`, `m-4` | Standard padding for cards, margins. |
| `spacing-6` | 24px | 1.5rem | `p-6`, `m-6` | Modals, large card paddings. |
| `spacing-8` | 32px | 2rem | `p-8`, `gap-8` | Section vertical rhythm. |
| `spacing-12`| 48px | 3rem | `py-12` | Major page sections. |
| `spacing-16`| 64px | 4rem | `py-16` | Landing page hero spacing. |

**Container Widths:**
*   Maximum main content width: `1200px` (`max-w-6xl`) to maintain line length readability.

---

## SECTION 6 — Layout Principles

*   **Containers:** Main dashboard content is wrapped in a centered container (`max-w-6xl w-full mx-auto`) to prevent horizontal stretching on ultra-wide monitors.
*   **Grids:** Use 12-column grids or CSS Grid (`grid-cols-1 md:grid-cols-2 lg:grid-cols-4`) for aligning stat cards and complex layouts.
*   **Cards:** Wrap grouped data (like "API Key Details") inside `Card` primitives to establish distinct visual boundaries.
*   **Responsive Behavior:** Stack columns vertically on mobile. Expand to horizontal layouts at the `md:` (768px) breakpoint.

---

## SECTION 7 — Elevation

Elevation communicates hierarchy, especially in dark mode where shadows are less visible. We use borders and subtle background shifts.

| Level | Application | Dark Mode Implementation | Light Mode Implementation |
| :--- | :--- | :--- | :--- |
| **Level 0** | Page Background | `bg-zinc-950` | `bg-white` |
| **Level 1** | Cards, Sidebar | `bg-zinc-900`, `border-zinc-800` | `bg-zinc-50`, `border-zinc-200` |
| **Level 2** | Dropdowns, Modals | `bg-zinc-800`, `ring-1 ring-white/10`| `bg-white`, `shadow-lg`, `ring-1 ring-black/5`|

---

## SECTION 8 — Motion System

Motion must be fast and purposeful.

*   **Page Transitions:** Instant. No fade-ins between routes to prioritize speed.
*   **Dialogs / Modals:** `duration-200 ease-out`, fading in while scaling up from `95%` to `100%`.
*   **Hover States:** `duration-150 ease-in-out` on buttons, transitioning background colors.
*   **Focus States:** Instant appearance of focus rings.
*   **Loading:** Skeletons pulse continuously (`animate-pulse`). Buttons display a spinning `<Loader2 />` icon.
*   **Reduced Motion:** Respect `prefers-reduced-motion: reduce` by disabling non-essential CSS transitions.

---

## SECTION 9 — Iconography

*   **Library:** Lucide React.
*   **Icon Size:** Standard `size-4` (16x16px) or `size-5` (20x20px).
*   **Stroke Width:** `strokeWidth={2}` for standard icons.
*   **Alignment:** Icons placed next to text must be vertically centered with a `gap-2` (8px).
*   **Usage Rules:** Use icons to supplement text, rarely as the sole indicator (except for standard actions like 'Close').

---

## SECTION 10 — Accessibility

*   **Contrast Ratios:** All text must meet WCAG 2.1 AA (4.5:1 for normal text, 3:1 for large text). The Zinc palette guarantees this natively.
*   **Keyboard Navigation:** All interactive elements (`<button>`, `<a>`, `<input>`) must be fully navigable via `Tab`.
*   **Focus Rings:** Visible focus rings (`focus-visible:ring-2 focus-visible:ring-indigo-500`) are mandatory. Never apply `outline: none` without a fallback.
*   **ARIA Considerations:** Dialogs must have `aria-modal="true"`. Expandable areas require `aria-expanded`.
*   **Color Blindness:** Never rely solely on color to convey meaning. Errors must have an icon (e.g., `<AlertTriangle />`) and textual explanation, not just red borders.

---

## SECTION 11 — Theme Strategy

APIMeter utilizes a robust dual-theme system powered by CSS variables and `next-themes`.

*   **Dark Mode (Default):** Activated via the `.dark` class applied to the HTML root.
*   **Light Mode:** Activated when `.dark` is removed.
*   **CSS Variables:** Tailwind utilities (`bg-background`, `text-foreground`) dynamically point to the correct HEX values injected into the `:root` and `.dark` CSS scopes.
*   **Theme Switching:** A toggle in the top navigation allows users to cycle between `light`, `dark`, and `system` preferences without page reloads or Flash of Unstyled Content (FOUC).

---

## SECTION 12 — Responsive Design

APIMeter is Mobile-First but optimized heavily for Desktop SaaS usage.

| Breakpoint | Width | Behavior |
| :--- | :--- | :--- |
| `sm` | `640px` | Expand mobile menus, allow cards to sit side-by-side. |
| `md` | `768px` | Convert stacked forms into two-column layouts. |
| `lg` | `1024px` | Expose the Desktop Sidebar, hide mobile Hamburger menu. |
| `xl` | `1280px` | Expand maximum width boundaries for ultra-wide displays. |

*   **Typography Scaling:** Use Tailwind fluid typogrpahy approaches or standard breakpoint prefixing (`text-sm md:text-base`).
*   **Component Adaptation:** Modals become full-screen bottom sheets on mobile.

---

## SECTION 13 — Quality Checklist

- [x] Design Principles documented.
- [x] Color scale defined matching the strict UX Blueprint.
- [x] Typography pairings (Inter + JetBrains Mono) explicitly designated.
- [x] 8px Spacing system established.
- [x] Elevation hierarchies established for Dark/Light modes.
- [x] Fast, purposeful motion guidelines set.
- [x] Accessibility rules (Keyboard focus, ARIA, contrast) mandated.
- [x] Tailwind CSS token strategy completely mapped.

---
*End of Design System Specification*
