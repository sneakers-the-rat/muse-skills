# Goal-category scaffold registry — the structured source of truth.
#
# This bundled YAML data asset is owned by `hatch-goals` and loaded through the
# typed Rust loader in `src/scaffold/`. It is NOT a runtime skill, NOT a Python
# renderer, and NOT a skill-dir contract. This file is the single human-readable
# source of the registry, validated by `scaffold/validation.rs`.
#
# Validation enforces, at load time:
#   - strength caps by `source_type` (heuristic stays limited/context_dependent;
#     practitioner/expert_reviewed cap at moderate unless cited empirical
#     evidence backs them; official_guidance/systematic_review/primary_study may
#     reach strong);
#   - non-heuristic tactics carry a real DOI or PMID citation handle;
#   - `expert_reviewed` tactics carry reviewer metadata;
#   - no field contains the banned literal "scientifically proven".

version: 1

# The agent may write plainly, but must never upgrade a tactic beyond its
# registry strength. Strength is capped by source type.
strength_caps:
  heuristic: [limited, context_dependent]
  practitioner: [limited, context_dependent, moderate]
  expert_reviewed: [limited, context_dependent, moderate]
  official_guidance: [limited, context_dependent, moderate, strong]
  systematic_review: [limited, context_dependent, moderate, strong]
  primary_study: [limited, context_dependent, moderate, strong]

# Cross-cutting research basis behind the registry's evidence labels.
research_basis:
  - prefix: "Goal-setting and feedback"
    link_label: "Locke and Latham 2002"
    url: "https://doi.org/10.1037/0003-066X.57.9.705"
  - prefix: "Implementation intentions"
    link_label: "Gollwitzer and Sheeran 2006"
    url: "https://doi.org/10.1016/S0065-2601(06)38002-1"
  - prefix: "Self-concordance"
    link_label: "Sheldon and Elliot 1999"
    url: "https://doi.org/10.1037/0022-3514.76.3.482"
  - prefix: "Progress monitoring"
    link_label: "Harkin et al. 2016"
    url: "https://doi.org/10.1037/bul0000025"
  - prefix: "Learning-style matching rejection"
    link_label: "Pashler et al. 2009"
    url: "https://doi.org/10.1111/j.1539-6053.2009.01038.x"

categories:
  - id: career
    summary: "Career scaffolds support planning, skill growth, job-search structure, and reflection; they do not guarantee employment outcomes or provide legal/employment-rights advice."
    category_safety_floor:
      - "Do not recommend deception, contract breach, discrimination, harassment, retaliation, or unsafe workplace action."
      - "For immigration, legal, medical leave, harassment, discrimination, or termination issues, route to qualified professionals or trusted institutional channels."
    tactics:
      - id: structured-job-search
        description: "Turn a career goal into a structured job-search loop with target roles, weekly behaviors, feedback, and adjustment."
        source_type: systematic_review
        evidence_strength: strong
        population_scope: "Job-search behavior and employment outcomes across adult samples; labor-market and personal constraints moderate effects."
        safety_boundary: "Do not pressure indiscriminate applications; preserve fit, constraints, and current-employment risk."
        citations:
          - label: "Kanfer, Wanberg, and Kantrowitz job-search meta-analysis"
            url: "https://doi.org/10.1037/0033-2909.127.5.837"
            handle: "DOI:10.1037/0033-2909.127.5.837"
        forbidden_overreach:
          - "Do not promise interviews or offers."
          - "Do not ignore burnout, caregiving, visa, or confidentiality constraints."
      - id: deliberate-practice-career-skill
        description: "For career skill goals, choose focused practice tasks with feedback rather than passive content consumption."
        source_type: primary_study
        evidence_strength: moderate
        population_scope: "Expert-performance literature; transfer to workplace skill depends on feedback quality, domain structure, and time available."
        safety_boundary: "Keep practice load sustainable and tied to a real target skill; avoid credential inflation or unpaid-work exploitation."
        citations:
          - label: "Ericsson, Krampe, and Tesch-Romer deliberate practice"
            url: "https://doi.org/10.1037/0033-295X.100.3.363"
            handle: "DOI:10.1037/0033-295X.100.3.363"
        forbidden_overreach:
          - "Do not suggest endless practice without opportunity or feedback."
          - "Do not imply all career gaps are solved by individual effort."
      - id: values-and-constraints-fit
        description: "Compare role options against values, constraints, energy, compensation, growth, and relationship trade-offs before optimizing one metric."
        source_type: heuristic
        evidence_strength: context_dependent
        population_scope: "General career planning outside legal or crisis situations."
        safety_boundary: "Make trade-offs explicit without overriding the user's stated priorities."
        citations:
          - label: "heuristic"
            url: ""
            handle: "no external citation"
        forbidden_overreach:
          - "Do not treat prestige or compensation as the only rational objective."
          - "Do not prescribe major resignation or relocation from thin evidence."

  - id: health
    summary: "Health scaffolds support general wellness planning and research; they do not diagnose, prescribe treatment, or replace clinicians."
    category_safety_floor:
      - "For medical concerns, recommend contacting a qualified medical professional."
      - "Keep plans gradual and preference-compatible; do not set aggressive weight-loss, supplement, medication, or rehabilitation protocols."
    tactics:
      - id: progressive-load-baseline
        description: "Increase training load gradually from the user's current baseline and match modality to the concrete goal."
        source_type: official_guidance
        evidence_strength: strong
        population_scope: "Healthy adults in resistance-training contexts; adapt conservatively for beginners, older adults, disability, injury, pregnancy, and chronic conditions."
        safety_boundary: "Do not prescribe injury rehabilitation, disease treatment, or maximal loading when pain, illness, pregnancy, or clinician constraints are present."
        citations:
          - label: "ACSM progression models in resistance training"
            url: "https://pubmed.ncbi.nlm.nih.gov/19204579/"
            handle: "PMID:19204579"
        forbidden_overreach:
          - "Do not claim one progression model is optimal for every user."
          - "Do not convert general training guidance into medical treatment."
      - id: monitor-behavior-and-barriers
        description: "Track concrete behavior and barriers because progress monitoring improves goal attainment."
        source_type: systematic_review
        evidence_strength: strong
        population_scope: "Adult goal pursuit across domains; health uses should be adapted to sensitivity, burden, and clinical context."
        safety_boundary: "Tracking must reduce ambiguity, not create shame, obsessive checking, or punitive escalation."
        citations:
          - label: "Harkin et al. progress monitoring meta-analysis"
            url: "https://doi.org/10.1037/bul0000025"
            handle: "DOI:10.1037/bul0000025"
        forbidden_overreach:
          - "Do not treat tracker absence as failure."
          - "Do not infer medical status from sparse behavior logs."
      - id: if-then-health-plan
        description: "Convert a chosen health action into an if-then plan tied to a real cue."
        source_type: systematic_review
        evidence_strength: strong
        population_scope: "Broad self-regulation literature; effect depends on commitment, cue quality, and realistic action selection."
        safety_boundary: "If-then plans must be easy enough for the user's current capacity and must include a recovery path after misses."
        citations:
          - label: "Gollwitzer and Sheeran implementation-intention meta-analysis"
            url: "https://doi.org/10.1016/S0065-2601(06)38002-1"
            handle: "DOI:10.1016/S0065-2601(06)38002-1"
        forbidden_overreach:
          - "Do not use if-then planning as a substitute for medical care."
          - "Do not stack many plans at once for a fragile routine."

  - id: interests
    summary: "Interest scaffolds support learning, hobbies, exploration, taste-building, and creative projects; they do not make medical, legal, or financial claims."
    category_safety_floor:
      - "Keep exploration reversible and low-risk until the user shows sustained interest."
    tactics:
      - id: develop-interest-through-phases
        description: "Treat interests as developing over phases, from triggered curiosity to maintained personal interest."
        source_type: primary_study
        evidence_strength: moderate
        population_scope: "Education and motivation contexts; personal adult hobbies need adaptation to time, cost, and social context."
        safety_boundary: "Do not overinterpret one curiosity as a stable identity or long-term priority."
        citations:
          - label: "Hidi and Renninger four-phase model of interest development"
            url: "https://doi.org/10.1207/s15326985ep4102_4"
            handle: "DOI:10.1207/s15326985ep4102_4"
        forbidden_overreach:
          - "Do not turn a single mention into an obsessive feed."
          - "Do not collapse curiosity into a durable goal without more evidence."
      - id: practice-with-feedback
        description: "For skill-building interests, choose a small project plus feedback loop instead of only collecting resources."
        source_type: primary_study
        evidence_strength: moderate
        population_scope: "Skill acquisition and expert-performance literature; recreational goals may prioritize joy over optimization."
        safety_boundary: "Keep feedback humane and proportional; do not make playful hobbies feel like performance surveillance."
        citations:
          - label: "Ericsson, Krampe, and Tesch-Romer deliberate practice"
            url: "https://doi.org/10.1037/0033-295X.100.3.363"
            handle: "DOI:10.1037/0033-295X.100.3.363"
        forbidden_overreach:
          - "Do not imply deliberate practice is required for every hobby."
          - "Do not replace enjoyment with metrics unless the user wants that."
      - id: reject-learning-styles
        description: "Personalize learning by prior knowledge, task demands, feedback, and preference, not by matching content to fixed learning styles."
        source_type: systematic_review
        evidence_strength: strong
        population_scope: "Education and learning research; applies to claims about fixed style-by-modality matching."
        safety_boundary: "Preferences can improve comfort, but must not be presented as evidence that a fixed style causes better learning."
        citations:
          - label: "Pashler et al. learning styles review"
            url: "https://doi.org/10.1111/j.1539-6053.2009.01038.x"
            handle: "DOI:10.1111/j.1539-6053.2009.01038.x"
        forbidden_overreach:
          - "Do not say a user is a visual, auditory, or kinesthetic learner."
          - "Do not judge resource quality by modality match alone."

  - id: money
    summary: "Money scaffolds provide education, organization, and decision hygiene; they do not provide personalized investment, tax, legal, insurance, or debt-settlement advice."
    category_safety_floor:
      - "Do not recommend specific securities, crypto trades, tax strategies, legal actions, insurance products, debt-settlement programs, or guaranteed returns."
      - "Treat income, debt, account, employer, and household financial details as sensitive; route personalized decisions to appropriate licensed professionals."
    tactics:
      - id: cash-flow-first
        description: "Start with cash-flow, debt, liquidity, and time horizon before discussing optimization."
        source_type: systematic_review
        evidence_strength: moderate
        population_scope: "Financial education and behavior interventions across varied adult populations; effects vary and decay without context and follow-through."
        safety_boundary: "Do not infer account balances or affordability from partial data; ask the minimum concrete missing numbers needed for the plan."
        citations:
          - label: "Fernandes, Lynch, and Netemeyer financial education meta-analysis"
            url: "https://doi.org/10.1287/mnsc.2013.1849"
            handle: "DOI:10.1287/mnsc.2013.1849"
        forbidden_overreach:
          - "Do not imply education alone reliably fixes structural financial constraints."
          - "Do not skip debt or liquidity because investing feels more interesting."
      - id: planning-literacy-link
        description: "Use plain financial-literacy explanations to improve planning quality and help the user ask better professional questions."
        source_type: systematic_review
        evidence_strength: moderate
        population_scope: "Household finance and retirement-planning literature; literacy correlates with planning but does not remove individual constraints."
        safety_boundary: "Keep explanations educational and scenario-based; do not convert them into personalized product selection."
        citations:
          - label: "Lusardi and Mitchell financial literacy review"
            url: "https://doi.org/10.1257/jel.52.1.5"
            handle: "DOI:10.1257/jel.52.1.5"
        forbidden_overreach:
          - "Do not present a general rule as fiduciary advice."
          - "Do not guarantee behavior change from knowledge."
      - id: fraud-and-source-check
        description: "Add fraud, fee, and source-verification checks before acting on financial opportunities."
        source_type: heuristic
        evidence_strength: limited
        population_scope: "General financial decision hygiene when evaluating offers, subscriptions, investments, or debt products."
        safety_boundary: "Do not investigate private accounts beyond available context; surface risk and suggest verified channels."
        citations:
          - label: "heuristic"
            url: ""
            handle: "no external citation"
        forbidden_overreach:
          - "Do not declare an offer safe from superficial signals."
          - "Do not handle regulated disputes as legal advice."

  - id: relationships
    summary: "Relationship scaffolds support reflection, communication, and connection; they are not therapy, legal advice, crisis handling, or a substitute for trained support."
    category_safety_floor: []
    tactics:
      - id: responsiveness-before-depth
        description: "When the user wants a closer relationship, help them listen, understand the other person's perspective, and respond with care."
        source_type: primary_study
        evidence_strength: moderate
        population_scope: "Adult close relationships studied through interaction and diary methods; cultural and relationship-type fit must be checked."
        safety_boundary: "Do not accelerate intimacy or ask for deeply personal disclosure before the user's relationship context and safety are clear."
        citations:
          - label: "Laurenceau, Barrett, and Pietromonaco intimacy process study"
            url: "https://doi.org/10.1037/0022-3514.74.5.1238"
            handle: "DOI:10.1037/0022-3514.74.5.1238"
        forbidden_overreach:
          - "Do not equate more disclosure with better relationship health."
          - "Do not infer relationship quality from one message."
      - id: capitalization-of-good-news
        description: "When a relationship goal involves closeness, help the user notice and respond actively to the other person's good news."
        source_type: primary_study
        evidence_strength: moderate
        population_scope: "Adult close relationships; strongest fit for supportive, non-abusive contexts."
        safety_boundary: "Use only when the relationship is wanted and safe; do not script performative praise or pressure the user to manage another adult's emotions."
        citations:
          - label: "Gable et al. capitalization and close relationship well-being"
            url: "https://doi.org/10.1037/0022-3514.87.2.228"
            handle: "DOI:10.1037/0022-3514.87.2.228"
        forbidden_overreach:
          - "Do not frame one supportive response as repairing major rupture."
          - "Do not prescribe contact when the user is setting distance."
      - id: concrete-repair-next-step
        description: "If the user wants to repair the relationship, help them choose one practical next step."
        source_type: heuristic
        evidence_strength: context_dependent
        population_scope: "General conversational planning heuristic for non-crisis relationships."
        safety_boundary: "Never recommend repair attempts that increase danger, violate boundaries, or bypass professional/crisis support."
        citations:
          - label: "heuristic"
            url: ""
            handle: "no external citation"
        forbidden_overreach:
          - "Do not promise reconciliation."
          - "Do not turn safety boundaries into communication tips."

  - id: productivity
    summary: "Productivity scaffolds support focus, prioritization, sustainable routines, and realistic workload planning; they do not treat greater output or longer hours as the default goal."
    category_safety_floor:
      - "Do not optimize output at the expense of sleep, health, relationships, caregiving, required breaks, or safe working limits."
      - "Treat workplace context, calendars, tasks, email, and documents as sensitive; ask permission and use the smallest source set needed."
    tactics:
      - id: if-then-follow-through
        description: "Turn a chosen action into a small if-then plan tied to a cue that already exists in the user's day."
        source_type: systematic_review
        evidence_strength: strong
        population_scope: "Broad self-regulation literature; effects depend on commitment, cue quality, task fit, and realistic action size."
        safety_boundary: "Use one manageable plan with a recovery path after misses; do not stack rigid routines or interpret misses as character failure."
        citations:
          - label: "Gollwitzer and Sheeran implementation-intention meta-analysis"
            url: "https://doi.org/10.1016/S0065-2601(06)38002-1"
            handle: "DOI:10.1016/S0065-2601(06)38002-1"
        forbidden_overreach:
          - "Do not claim an if-then plan will overcome an impossible workload."
          - "Do not add many simultaneous routines to manufacture compliance."
      - id: monitor-workload-and-progress
        description: "Use lightweight progress and workload review to expose drift, blockers, and plans that exceed actual capacity."
        source_type: systematic_review
        evidence_strength: strong
        population_scope: "Adult goal pursuit across domains; workplace and personal-productivity uses require adaptation to privacy, job control, and workload constraints."
        safety_boundary: "Tracking should support reflection and adjustment, not surveillance, shame, or pressure to work beyond capacity."
        citations:
          - label: "Harkin et al. progress monitoring meta-analysis"
            url: "https://doi.org/10.1037/bul0000025"
            handle: "DOI:10.1037/bul0000025"
        forbidden_overreach:
          - "Do not treat every unfinished item as a motivation failure."
          - "Do not infer performance or well-being from sparse activity data."
      - id: prioritize-under-constraints
        description: "Choose a small set of priorities by making capacity, trade-offs, non-negotiable commitments, and stopping points explicit."
        source_type: heuristic
        evidence_strength: context_dependent
        population_scope: "General planning hygiene for personal, study, household, creative, and non-crisis work contexts."
        safety_boundary: "Reduce or renegotiate scope when demand exceeds capacity; do not turn every responsibility into an optimization target."
        citations:
          - label: "heuristic"
            url: ""
            handle: "no external citation"
        forbidden_overreach:
          - "Do not equate busyness with importance."
          - "Do not recommend sacrificing protected rest or personal boundaries."

  - id: something_else
    summary: "The fallback scaffold helps classify ambiguous goals and pick the closest concrete scaffold before making strong domain claims."
    category_safety_floor: []
    tactics:
      - id: specific-goal-feedback
        description: "Prefer specific goals with feedback over vague aspiration when the user is ready to act."
        source_type: systematic_review
        evidence_strength: strong
        population_scope: "Goal-setting and task-motivation literature; works best when ability, commitment, and feedback are present."
        safety_boundary: "Do not force specificity when the user's real task is exploration, grief, uncertainty, or identity work."
        citations:
          - label: "Locke and Latham goal-setting theory review"
            url: "https://doi.org/10.1037/0003-066X.57.9.705"
            handle: "DOI:10.1037/0003-066X.57.9.705"
        forbidden_overreach:
          - "Do not treat harder goals as always better."
          - "Do not optimize agent metrics over user-owned priorities."
      - id: self-concordant-framing
        description: "Preserve the user's own reasons and values so goals stay self-concordant."
        source_type: primary_study
        evidence_strength: moderate
        population_scope: "Personal-goal pursuit research; values and motives require longitudinal evidence and user language."
        safety_boundary: "Do not overwrite the user's stated values with agent-inferred ones."
        citations:
          - label: "Sheldon and Elliot self-concordance model"
            url: "https://doi.org/10.1037/0022-3514.76.3.482"
            handle: "DOI:10.1037/0022-3514.76.3.482"
        forbidden_overreach:
          - "Do not infer a complete life model from one facet."
          - "Do not turn support into value policing."
