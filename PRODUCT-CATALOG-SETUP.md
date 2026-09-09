# Wildfyre product catalogue setup

Shopify product records and collection membership are store data and cannot be created by a theme deployment. Create the following six products in **Shopify Admin → Products**. Use the listed title as the product title and handle.

| Product | Handle | Tags / automated collections |
| --- | --- | --- |
| Amalfi | `amalfi` | `Men` |
| Wild Chills | `wild-chills` | `Men`, `Unisex` |
| Tobacco Money | `tobacco-money` | `Men` |
| Oud for Darknights | `oud-for-darknights` | `Men`, `Unisex` |
| Butterfly Kisses | `butterfly-kisses` | `Women` |
| Intimissi | `intimissi` | `Women` |

Create (or retain) the `men`, `women`, and `unisex` collections as **automated collections** with the rule **Product tag is equal to** their respective tag. This lets Wild Chills and Oud for Darknights appear in Men and Unisex without creating duplicate products. The existing `/collections/men`, `/collections/women`, and `/collections/unisex` links and collection template will then work without theme changes.

Add the supplied product copy to each product's standard **Description** field. For reusable fragrance details, define these product metafields in **Settings → Custom data → Products**, all as *Single line text*:

`custom.main_notes`, `custom.top_notes`, `custom.heart_notes`, and `custom.base_notes`.

The theme displays these metafields in the existing product accordion styling. Until they are entered in Admin, it provides the supplied note data for the six handles above as a fallback. Store the descriptions in Shopify Admin to preserve native product SEO and make them available outside the product template.

| Product | Main notes | Top notes | Heart notes | Base notes |
| --- | --- | --- | --- | --- |
| Wild Chills | Bergamot · Ozonic Accord · Marine Notes · Herbal Tea · Sandalwood · Musk | Bergamot · Orange · Marine Accord | Herbal Tea · Ozonic Accord | Sandalwood · Musk |
| Amalfi | Bergamot · Lavender · Cedarwood | Bergamot · Icy Accord | Lavender · Geranium · Citrus Accord | Cedarwood · Amber · Musk |
| Oud for Darknights | Sensual Fruits · Berries · Oud · Musk · Patchouli | Sensual Berries · Nutmeg · Lavender | Agarwood (Oud) | Patchouli · Musk |
| Tobacco Money | Tobacco Leaves · Spices · Creamy Vanilla · Woods | Tobacco Leaf · Spices | Vanilla · Tonka Bean · Cacao | Woody Notes · Amber · Musk |
| Butterfly Kisses | Juicy Berries · Mandarin Orange · Jasmine · Vanilla · Amber Resin · Woods | Blackcurrant · Strawberry · Mandarin Orange | Jasmine · Vanilla | Warm Amber · Patchouli · Oakmoss |
| Intimissi | Jasmine · Jasmine Sambac · Orange Blossom · Warm Amber · Vanilla | Jasmine Sambac · Ambergris | Vanilla · Orange Blossom | Sandalwood · Warm Amber · Vanilla Absolute |
