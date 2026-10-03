# SOVOS Routine Packs

**Status:** CURRENT starter pack catalog  
**Effective:** 2026-10-03  
**Schema:** `contracts/operator-routine-pack.v1.schema.json`

Routine Packs are composable suggestion bundles used by the audit and Portfolio Business Compiler to recommend coherent groups of Routine Templates for a life domain or business operating shape.

A pack is **not a classification of a person or company**. One owner or business can match several packs, and every template still requires evidence/fit review before it becomes an owner-specific Routine Candidate/Blueprint.

## Life-domain packs

- `life-personal-executive.json`
- `life-household-family.json`
- `life-research-creator.json`
- `life-personal-finance.json`
- `life-wellness-care.json`

## Business and portfolio packs

- `business-professional-services.json`
- `business-software-saas.json`
- `business-content-community.json`
- `business-ecommerce-product.json`
- `business-local-field-service.json`
- `business-founder-portfolio.json`

These packs intentionally overlap. A founder may also be a creator and household administrator; a business may combine software, services, commerce and community. Composition follows evidence and owner goals rather than assigning a rigid identity.

Use packs to improve discovery coverage, not to manufacture work that does not exist. A suggestion created only because a pack matches must remain labeled **archetype suggestion; recurrence not yet evidenced** until current evidence or owner declaration supports it.

~~~text
audit evidence
→ candidate
→ pack/template suggestions
→ explicit fit reasoning
→ owner-specific blueprint
→ determinization
→ compiled instance
~~~

Pack references are regression-tested against the canonical `routine-templates/` catalog. A pack may suggest a routine; it cannot create authority, a worker, a schedule or an external effect.
