---
name: Perfume Pharmacy
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f4'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#4c4546'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#7e7576'
  outline-variant: '#cfc4c5'
  surface-tint: '#5e5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1b1b1b'
  on-primary-container: '#848484'
  inverse-primary: '#c6c6c6'
  secondary: '#5e5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e1dfdf'
  on-secondary-container: '#626262'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#1a1c1c'
  on-tertiary-container: '#838484'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e2e2e2'
  primary-fixed-dim: '#c6c6c6'
  on-primary-fixed: '#1b1b1b'
  on-primary-fixed-variant: '#474747'
  secondary-fixed: '#e4e2e2'
  secondary-fixed-dim: '#c7c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-lg:
    fontFamily: EB Garamond
    fontSize: 48px
    fontWeight: '500'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: EB Garamond
    fontSize: 36px
    fontWeight: '500'
    lineHeight: '1.1'
  headline-md:
    fontFamily: EB Garamond
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
  headline-sm:
    fontFamily: EB Garamond
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.2'
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Hanken Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  mono-data:
    fontFamily: Hanken Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: -0.01em
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
---

## Brand & Style

The design system is built on the narrative of the "Perfume Pharmacy"—a clinical, authoritative, and transparent approach to high-end fragrance. The objective is to demystify luxury perfumery by stripping away the marketing fluff and replacing it with functional data and clear typography.

The aesthetic follows a **Minimalist / High-Contrast** movement. It utilizes a stark white background and aggressive black typography to mirror the efficiency of a laboratory dossier. The emotional response should be one of intellectual trust; the user is not being "sold" a dream, but rather provided an expert prescription. The UI remains premium through meticulous whitespace and refined serif accents, yet stays accessible through its utilitarian structure.

## Colors

The palette is strictly monochromatic to emphasize clarity and clinical authority.

- **Primary (#000000):** Used for all critical information, headlines, and primary CTA backgrounds. It represents the "ink" of a formal dossier.
- **Secondary (#666666):** Used for metadata, scent intensity scales, and supporting text to create hierarchy without introducing color.
- **Tertiary (#E5E5E5):** Reserved for structural dividers, table borders, and subtle background zones in education blocks.
- **Neutral (#FFFFFF):** The foundation of the system. Excessive whitespace is required to maintain the high-contrast, minimalist aesthetic.

Functional states (Success, Error) should avoid traditional green/red in favor of bold black icons or underlined text treatments to maintain the "Pharmacy" rigor, unless accessibility requirements dictate otherwise.

## Typography

This design system employs a "Dual-Type" strategy to balance luxury and utility.

**EB Garamond** is used for headlines and editorial titles. It provides the "premium" weight, evoking the feeling of a classic apothecary or a heritage luxury brand. It should be typeset with tight leading and slight negative letter-spacing for a modern, editorial look.

**Hanken Grotesk** is the workhorse for all functional data. It is a sharp, contemporary sans-serif that ensures high legibility for price comparisons, scent notes, and technical descriptions. 

Use the `label-caps` style for all section headers and "Why Saffron?" educational labels to signify an authoritative classification.

## Layout & Spacing

The layout is governed by a **Strict Laboratory Grid**. 

- **Grid:** Use a 12-column grid for desktop and a 4-column grid for mobile. Elements should be aligned to the grid with zero "visual fluff."
- **Rhythm:** Spacing follows a base-4 scale. Use `lg` (48px) or `xl` (80px) to separate major sections, creating the "breathe" required for a minimalist aesthetic.
- **Borders:** Instead of shadows, use 1px solid lines (#E5E5E5 or #000000) to define layout boundaries, reminiscent of a printed form or technical manual.
- **Reflow:** On mobile, price tables and comparison blocks should shift from side-by-side to stacked vertical lists, maintaining a 1px divider between rows.

## Elevation & Depth

This design system avoids shadows and depth entirely to maintain its clinical, "flat" dossier identity. 

- **Tonal Layers:** Visual hierarchy is achieved through contrast and containment. A section might have a light grey (#F9F9F9) background to distinguish it from the main white canvas, but it will never "float."
- **Functional Overlays:** Modals and menus use sharp 1px black borders. Backdrops should be a high-opacity white blur to maintain focus without introducing dark "heavy" shadows.
- **Low-Contrast Outlines:** For secondary UI elements like inactive input fields, use a soft #E5E5E5 border. Active elements switch immediately to 1.5px solid Black.

## Shapes

The shape language is **Sharp (0)**. 

Every element—buttons, input fields, image containers, and cards—must have 0px corner radii. This reinforces the "clinical" and "architectural" nature of the brand. Rounded corners are seen as too soft and consumer-centric for this specific "Perfume Pharmacy" narrative.

Images of perfume bottles should be framed in strict rectangular containers, often with a 1px border to treat the photography like a specimen in a slide.

## Components

**Buttons:** 
Primary buttons are solid black rectangles with white `label-caps` typography. Secondary buttons use a 1px black outline with black text. No hover transitions should involve color; instead, use a slight opacity shift or an "Invert" effect (Black to White).

**Comparison Tables:**
Used for "Our Scent vs. Luxury Scent." Use 1px #E5E5E5 horizontal dividers. Headers should be in `label-caps`. The "Our Scent" column should be highlighted with a very subtle grey background or a bold left-border.

**Scent Intensity Scales:**
A horizontal 10-segment bar. Filled segments are solid black; unfilled segments are #E5E5E5. This provides a data-driven visual of the fragrance's strength.

**Educational 'Why' Blocks:**
Contained in a 1px black border box. The title uses `headline-sm` (Serif) to signal authority, while the body uses `body-md` (Sans) for clear information delivery.

**Input Fields:**
Strict rectangular boxes with 1px #E5E5E5 borders. Labels sit above the field in `label-caps`. Focus state is a 1.5px Black border.