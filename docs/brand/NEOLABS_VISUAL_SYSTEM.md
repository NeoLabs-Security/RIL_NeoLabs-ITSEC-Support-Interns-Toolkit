# NeoLabs IT Security Support Toolkit Visual System

## Brand purpose

Every student guide, support playbook, lab pack and template should look like one official **NeoLabs × RIL Cybersecurity Internship** publication while remaining readable during practical troubleshooting.

## Wordmark

```text
NEOLABS
SECURITY LABS · IT SECURITY SUPPORT
```

Use the uppercase NeoLabs wordmark as the dominant cover element and Signal Cyan for the smaller track line.

## Colour palette

| Role | Hex | Use |
|---|---|---|
| NeoLabs Midnight | `#101A2B` | cover, major headings, footer |
| Signal Cyan | `#00A6C8` | rules, links, workflow markers |
| Analyst Blue | `#1F5F99` | secondary headings and callouts |
| Evidence Amber | `#D89216` | evidence/change cautions |
| Incident Red | `#B53838` | escalation/critical warnings |
| Slate | `#4B5563` | supporting text |
| Paper | `#F7F9FC` | page/callout background |
| White | `#FFFFFF` | cover text and contrast |

Colour must never be the only indicator of meaning.

## Typography

- headings: `DejaVu Sans`, `Arial`, sans-serif;
- body: `DejaVu Serif`, `Georgia`, serif;
- code: `DejaVu Sans Mono`, `Consolas`, monospace.

Do not commit font files.

## Page structure

Covers include NeoLabs wordmark, publication title, track, version/date and **Authorised synthetic training use only**. Running headers show `NEOLABS · IT SECURITY SUPPORT`; footers show classification and page number.

## Support callouts

Use these labels consistently:

- **Support note** — interpretation/troubleshooting advice;
- **Evidence requirement** — state/timestamps/details that must be recorded;
- **Change boundary** — actions requiring explicit approval;
- **Rollback check** — what must exist before a change;
- **SOC escalation** — when evidence should be handed to the SOC track;
- **Validation check** — how to prove service/account recovery.

## Tables, code and screenshots

Tables use Midnight headers and alternating light rows. Code blocks use a light background and cyan left rule. Commands that change configuration must be clearly separated from read-only diagnostics and must include approval/rollback context.

Screenshots must be readable, captioned and redacted. Never include Access Codes, broker sessions, private keys, real user data or unrelated pod information.

## Accessibility

Body text should render at approximately 10.5-11.5 pt with at least 1.35 line spacing. Heading hierarchy must remain semantic. Links should be recognisable without relying only on colour.

## Approval

A publication is ready only after technical, safety, editorial and PDF render checks pass. Generated PDFs must not contain live credentials or private infrastructure details.
