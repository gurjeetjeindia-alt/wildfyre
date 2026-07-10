---
name: Ethereal Essence
colors:
  surface: '#fdf8f8'
  surface-dim: '#ddd9d8'
  surface-bright: '#fdf8f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f7f3f2'
  surface-container: '#f1edec'
  surface-container-high: '#ebe7e6'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1c1b1b'
  on-surface-variant: '#444748'
  inverse-surface: '#313030'
  inverse-on-surface: '#f4f0ef'
  outline: '#747878'
  outline-variant: '#c4c7c7'
  surface-tint: '#5f5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1c1b1b'
  on-primary-container: '#858383'
  inverse-primary: '#c8c6c5'
  secondary: '#5e5f5b'
  on-secondary: '#ffffff'
  secondary-container: '#e3e3de'
  on-secondary-container: '#646561'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#241a09'
  on-tertiary-container: '#91826a'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#e3e3de'
  secondary-fixed-dim: '#c7c7c2'
  on-secondary-fixed: '#1b1c19'
  on-secondary-fixed-variant: '#464744'
  tertiary-fixed: '#f3e0c4'
  tertiary-fixed-dim: '#d6c4aa'
  on-tertiary-fixed: '#241a09'
  on-tertiary-fixed-variant: '#514531'
  background: '#fdf8f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  headline-xl:
    fontFamily: Playfair Display
    fontSize: 64px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  label-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  container-max: 1440px
  gutter: 32px
  margin-desktop: 80px
  margin-mobile: 20px
  stack-xl: 120px
  stack-lg: 80px
  stack-md: 40px
---

## Brand & Style
The design system is rooted in **Modern Minimalism** with a strong **Editorial** influence. It targets a discerning audience that values slow luxury, olfactory art, and quiet sophistication. The visual narrative is built on the tension between high-contrast typography and vast, airy compositions.

The UI must evoke a sense of calm, exclusivity, and tactile quality. Every element is intentional; whitespace is treated not as "empty" but as a premium structural component that allows product photography to breathe. The emotional response should be one of curated refinement—like walking into a high-end boutique where only a few items are displayed at a time.

## Colors
The palette is a sophisticated interplay of organic neutrals and deep obsidian. 

- **Primary (#121212):** Used for typography, icons, and high-impact CTAs to ensure maximum legibility and a "premium ink" feel.
- **Background (#F9F8F3):** A "Bone White" that provides a warmer, more human touch than pure white, reducing eye strain and feeling more like heavy-stock paper.
- **Tertiary (#B5A48B):** A muted metallic gold used sparingly for micro-details, dividers, or luxury badges.
- **Surface (#F0F0F0):** A soft light grey specifically reserved for product card backgrounds to provide a subtle lift from the main page body.
- **Accent Sage (#9BA89B):** An alternative muted tone for secondary informative elements or specific scent category identifiers.

## Typography
The typography system relies on a "High-Contrast Pairing" strategy. 

**Playfair Display** handles all editorial storytelling. It should be used for large hero statements, product names, and section headers. Tight letter spacing is applied to larger sizes to maintain a compact, fashionable look.

**Inter** provides the functional backbone. It is used for body descriptions, navigation, and interface labels. Its neutral, systematic nature balances the expressive qualities of the serif. Use `label-caps` for category headers and utility links to provide a rhythmic contrast to the fluid body text.

## Layout & Spacing
This design system utilizes a **Fixed Grid** philosophy on desktop and a **Fluid Margin** approach on mobile. The layout is intentionally sparse.

- **Desktop:** 12-column grid with wide 80px margins to frame the content like a gallery wall.
- **Vertical Rhythm:** Large gaps (`stack-xl`) between sections are mandatory to prevent visual clutter and signal the end of a narrative beat.
- **Photography:** Images should frequently break the grid or span full-bleed to create an immersive, magazine-like experience. 
- **Alignment:** Use asymmetrical layouts—placing text in a 4-column span next to a 6-column image—to create visual interest without relying on heavy decorative elements.

## Elevation & Depth
Depth is achieved through **Soft Tonal Layering** and **Ambient Shadows** rather than heavy borders.

1.  **The Base:** The Bone White background is the infinite canvas.
2.  **The Lift:** Product cards and modals use the `surface` color (#F0F0F0) to create a subtle chromatic shift.
3.  **Shadows:** Use extremely diffused, low-opacity shadows (e.g., `0px 20px 40px rgba(0,0,0,0.03)`). Shadows should feel like the object is caught in soft, natural morning light.
4.  **Glassmorphism:** Reserved exclusively for the global navigation bar. A 20px backdrop blur with 80% opacity of the background color allows the site content to shimmer through as the user scrolls, maintaining a sense of depth and continuity.

## Shapes
The shape language is primarily **Sharp and Architectural**. 

We use `roundedness: 1` (Soft) sparingly. Small radius (4px) is applied to buttons and input fields to take the "edge" off the brutalist tendencies, making the interface feel more approachable and modern. Product images should remain perfectly sharp (0px) to mimic the crisp edges of glass fragrance bottles and high-end editorial prints.

## Components

- **Buttons:** Primary buttons are solid Obsidian (#121212) with white Inter text. Secondary buttons are "Ghost" style with a 1px Obsidian border. All buttons use a subtle 4px corner radius. On hover, the primary button should shift to a dark grey with a fluid ease-in-out transition.
- **Product Cards:** These are the centerpiece. Use the Surface (#F0F0F0) background. On hover, the image should scale up by 3% (`scale(1.03)`) and the fragrance "Notes" (e.g., Bergamot, Cedar) should fade in as `label-caps` typography at the bottom of the card.
- **Input Fields:** Minimalist under-line style. Only the bottom border is visible (1px, #D1D1D1). On focus, the border transitions to Obsidian (#121212).
- **Navigation:** Top-aligned, high-transparency glass bar. Links are `label-caps` with a 1.2s transition underline effect on hover.
- **Chips/Labels:** Used for scent families (e.g., "Woody", "Floral"). These should be pill-shaped with the Sage (#9BA89B) background and white text, used at a very small scale.
- **Lists:** Clean, high-contrast rows with 1px light grey separators. Ensure generous vertical padding (24px+) between list items to maintain the premium feel.