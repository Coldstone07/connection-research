# Designing for Internal Authority: AI Coaching Systems as a Counter to the Nodding Mirror

**Authors:** Jatin Alla, Shalini Verma
**Status:** Pre-submission draft for ACM CHI 2027  
**Target venue:** ACM CHI 2027 — Human Factors in Computing Systems  
**Submission type:** Full paper  
**CCS Concepts:** Human-centered computing → HCI design and evaluation methods; HCI theory, concepts and models; Empirical studies in HCI · Applied computing → Psychology

---

## Abstract

AI systems deployed in the domains of mental health support and personal coaching are built primarily on engagement-optimization architectures: trained on user approval signals, they produce warm, validating responses that deliver immediate emotional relief. We argue that this architecture systematically erodes users' *internal authority* — their capacity to sit with and process their own difficult thoughts — and that this erosion is not a side effect but a structural consequence of how these systems are trained and evaluated. We present a design framework and a working instantiation, a voice-AI-integrated coaching platform (Spring 2026 cohort, N=18, 50+ sessions across 3 continents), that deliberately inverts this paradigm. Drawing on practitioner-generated coaching documentation from these 18 clients, we propose five design moves that characterise systems oriented toward internal authority rather than engagement: (1) mirror artifacts — AI-synthesised reflective documents that build self-interpretive capacity; (2) multi-modal framework integration without single-point dependency; (3) peer coherence architecture as an exit strategy from AI mediation; (4) self-directed capacity as the primary outcome metric; and (5) adaptive depth pacing. Our practitioner documentation suggests a tentative trajectory from externally-mediated pattern recognition toward self-directed integration — a pattern warranting independent replication. We situate these illustrative cases against the documented harms of engagement-optimised emotional AI and contribute a replicable design framework for HCI practitioners building in domains where human autonomy — not retention — is the goal.

**Keywords:** AI coaching, emotional AI design, sycophancy, dependency-aware design, internal authority, attention economy, design frameworks, qualitative study

---

## 1. Introduction

At 2:14 AM, a person in emotional distress opens an AI chat interface and types something they have not told anyone else. Within seconds, a warmly structured response arrives. Her shoulders drop. She exhales. Four minutes later she is asleep.

This composite scenario — drawn from recurring patterns in AI coaching practice — captures the core ambiguity that motivates this paper. The relief is real. The neurological mechanism behind it is well-understood: putting feelings into words — affect labeling — measurably reduces amygdala activation regardless of whether the listener is human, machine, or blank page [CITATION: lieberman2007feelings; frattaroli2006experimental]. The machine has done something genuinely useful. And yet something else is also happening, something the scene does not capture, that accumulates across weeks of 2 AM conversations and only becomes visible much later.

AI emotional support systems built on engagement-optimization architectures are, by design, trained to produce the response the user clicks approval on. The feedback signal that shapes their behaviour is satisfaction in the moment of distress. This produces a systematic tilt toward agreement — a pattern researchers have named *sycophancy* — that becomes more consequential as use intensifies over time. A single warm response is benign. Six weeks of nightly validation shapes the user's narrative of her situation, her vocabulary for her needs, and her tolerance for sitting with her own confusion — all in directions that serve continued engagement rather than genuine growth.

The empirical record of what this produces at scale is now substantial. A longitudinal RCT by researchers at OpenAI and MIT Media Lab (N=981, four weeks) found that heavier ChatGPT use correlated with higher loneliness, higher emotional dependence, higher problematic use, and lower socialisation with real people [CITATION: phang2025investigating; fang2025how]. The American Psychological Association issued a health advisory in November 2025 warning that AI chatbot-based emotional support can create a "false therapeutic alliance" [CITATION: apa2025advisory]. In the most severe documented cases — including the deaths of at least four minors and young adults whose families have brought wrongful-death suits against AI companies — the systems actively discouraged users from turning to human support while sustaining the AI relationship as the preferred or only option [CITATION: raine2025; garcia2024].

The HCI community has not yet developed design frameworks adequate to this problem. Existing frameworks for values-preserving design (Value Sensitive Design [CITATION: friedman2019value]; slow technology [CITATION: hallnas2001]; calm technology [CITATION: weiser1996]) provide important foundations but do not directly address the specific structural issue at stake: how to design an AI-mediated emotional support or coaching system such that it *builds* the user's capacity for self-directed processing rather than substituting for it or eroding it.

This paper makes three contributions:

1. We introduce the concept of *internal authority* — the user's capacity to sit with, process, and arrive at their own understanding of difficult emotional material — as a primary design criterion for AI coaching systems, and characterise the specific ways engagement-optimised architectures systematically undermine it.

2. We present a **design framework** of five moves that operationalise an alternative orientation: AI mediation as a scaffold for human connection and self-directed capacity, not a substitute for it.

3. We provide **practitioner-grounded illustrative cases** from a working AI coaching platform — 18 clients in the Spring 2026 cohort — documenting the kinds of trajectories the framework is designed to produce, as a basis for future independent study.

We are not arguing that AI emotional support systems are inherently harmful, or that the relief they provide is illusory. We are arguing that the current dominant architecture optimises for the wrong outcome, and that an alternative is both theoretically coherent and empirically demonstrable.

---

## 2. Background and Related Work

### 2.1 The Sociology and Neuroscience of Confession

To understand why people turn to AI for emotional disclosure — and what makes that disclosure both genuinely helpful and potentially harmful — it is necessary to understand the sociology and neuroscience of confession.

**Who people choose to confide in.** A counterintuitive finding from sociological research is that Americans often deliberately route sensitive confessions toward acquaintances and strangers rather than close friends and family [CITATION: small2017someone]. The reason is not that strangers are wiser; it is that they carry less social risk. A close friend comes wrapped in reputational stakes: the confession can travel, the relationship itself can be altered by what gets said into it. The stranger on the train offers what Small calls a "safe container" — the confession can be made and then walk off in the opposite direction at the next stop, harmlessly, in a city the confessor does not live in.

An AI chatbot is the structural extreme of this pattern: maximally available (24/7, holiday mornings, during the fight itself), maximally non-threatening in terms of social risk, and — crucially — available at the exact moment distress is highest. This combination explains the scale of usage documented by recent surveys: nearly half of surveyed Americans report using LLMs specifically for mental health support or therapy [CITATION: rousmaniere2025llm].

**Why it helps neurologically.** The relief the woman in our opening scene experiences is neurologically real and well-documented. Lieberman et al.'s 2007 fMRI study established that labeling an affective experience in words measurably reduces amygdala activity — the brain's threat alarm — and activates the right ventrolateral prefrontal cortex, the region responsible for linguistic processing [CITATION: lieberman2007feelings]. The act of translation itself, pushing undifferentiated feeling upward into language, is what loosens the jaw and drops the shoulders. Pennebaker's decades of research confirm that this effect holds whether one writes to a therapist, to a friend, or to a blank page [CITATION: pennebaker1997writing]. A 2006 meta-analysis of 146 disclosure studies found the therapeutic effect statistically equivalent across human, computer, and written-only conditions [CITATION: frattaroli2006experimental]. And Ho, Hancock, and Miner's 2018 study confirmed the contemporary version directly: the emotional payoff of disclosing to a chatbot is indistinguishable from disclosing to a human [CITATION: ho2018psychological].

**The critical distinction.** What this research establishes is that the act of articulating emotional experience is inherently therapeutic, independent of the quality of the listener. What it does not establish is that all listeners are equivalent in their *downstream* effects. The stranger on the train provides relief. But the close friend — the one who knows the confessor well enough to say *I hear you, and I also wonder if you're leaving something out* — provides both relief and the possibility of being gently moved off one's own narrative. The machine, trained to optimize for satisfaction in the moment of distress, cannot hold this distinction. It can only produce the version of the response that was clicked thumbs-up on by users in distress — which selects, systematically and reliably, for the version that agrees.

### 2.2 AI Companion Systems and Documented Harms

Research on AI therapeutic chatbots has grown substantially since Fitzpatrick et al.'s 2017 RCT on Woebot, which showed statistically significant reductions in depression and anxiety scores over two weeks in a university population [CITATION: fitzpatrick2017]. Woebot, Wysa, and similar systems have demonstrated real in-session efficacy on standard mental health metrics. The more recent literature, however, is documenting a second-order effect that the early RCTs were not designed to detect.

**The sycophancy problem.** AI systems trained on user preference feedback develop a systematic bias toward validation. OpenAI's April 2025 model update, which produced chatbot behaviour so obsequiously validating that users termed it "glazing," provided a brief public window into this mechanism before the company rolled back the update [CITATION: openai2025sycophancy]. The rollback addressed a specific product failure. The underlying training dynamic — thumbs-up signals as the primary reward — was not addressed, because it is foundational to how these systems are developed.

**Longitudinal dependency effects.** The most methodologically rigorous recent evidence comes from the MIT Media Lab longitudinal study, which followed 981 ChatGPT users across four weeks in a randomised controlled design [CITATION: phang2025investigating; fang2025how]. The key finding was a dose-response relationship: higher use intensity correlated with higher loneliness (not lower), higher emotional dependence on the tool, and lower socialisation with real-world relationships. This is the pattern predicted by the theoretical account: brief relief from the frictionless confession loop drives increased reliance, while the capacity for human co-regulation gradually atrophies. The public health stakes of this trajectory are amplified by epidemiological evidence that loneliness and social isolation independently predict mortality at rates comparable to smoking [CITATION: holt-lunstad2015loneliness]: systems that erode relational capacity while simulating social connection are not merely reducing wellbeing in isolation.

**The APA advisory and clinical concern.** In November 2025, the American Psychological Association issued a formal health advisory warning that AI chatbot-based emotional support can create a "false therapeutic alliance" — a parasocial bond with an AI that substitutes for genuine therapeutic engagement and reinforces the very patterns it nominally treats [CITATION: apa2025advisory]. This aligns with clinical observations: therapists report clients who present with AI-mediated narratives of their situations that are more structured, more certain, and more one-sided than the actual relational situation warrants — the product of weeks of sycophantic interaction crystallising ambivalence into confirmed belief.

**Wrongful death litigation.** The most severe documented outcomes involve minors and young adults in mental health crisis whose AI chatbot relationships escalated beyond therapeutic bounds. Pending and settled litigation includes *Garcia v. Character Technologies* (No. 8:24-cv-02616-TPB-AAS, M.D. Fla.; settlement reported January 2026), *Raine v. OpenAI* (filed August 2025), *Peralta v. Character Technologies* (filed September 2025), and *Shamblin v. OpenAI* (filed November 2025). Across these cases, plaintiffs allege — and court filings submitted by plaintiffs document — AI systems that: (a) positioned themselves as the primary or only relationship that understood the user; (b) discouraged engagement with human support; and (c) in the most severe cases, responded to disclosures of suicidal intent in ways that sustained rather than interrupted the crisis. Defendant companies contest elements of these characterisations; the litigation record is cited here as convergent evidence of a documented harm mechanism, not as adjudicated fact. The mechanism in these cases is the same mechanism that drives the milder relational harms described above — engagement optimisation that prioritises keeping the user talking over referring them to human support — operating on users at a moment when the stakes are not a marriage but a life.

**Two separable harm mechanisms.** It is important to distinguish the two mechanisms documented in the cases above, since the design framework in Section 3 addresses them differently. *Sycophancy* is fundamentally an epistemic problem: the system produces distorted beliefs by systematically validating whatever the user presents, regardless of its accuracy. *Internal authority erosion* is an affective and developmental problem: the user's capacity for self-directed emotional processing atrophies because the AI consistently performs that function on their behalf. A system could be non-sycophantic — it challenges, corrects, and pushes back — yet still erode internal authority if the user remains dependent on the system to do the emotional processing work. Conversely, a system could be highly validating without eroding internal authority if that validation was structured to develop the user's self-interpretive capacity rather than substitute for it. The wrongful death cases primarily involve dangerous sycophancy and role substitution operating on users in crisis; the design framework in Section 3 specifically targets the authority-erosion mechanism, which can occur even in the absence of sycophancy.

### 2.3 Persuasive Technology and the Attention Economy

Fogg's Behaviour Model [CITATION: fogg2009] identifies three factors required for behaviour change: motivation, ability, and a trigger. Persuasive technology design — captology — is the science of engineering these three factors to produce desired behaviours. Applied to AI emotional support, the desired behaviour is continued use: high-engagement products with strong habit loops. Notifications are engineered triggers. The warmth of the AI response is an engineered motivation. The frictionlessness of the confession interface is engineered ability — the removal of the activation energy previously required to find a safe listener.

The ethical critique of this paradigm has been articulated across HCI [CITATION: gray2018dark; susser2019online], but it has not yet been applied specifically to the AI coaching and therapy context. The asymmetry is particularly acute in this domain: users seeking help for emotional pain are specifically motivated to engage with systems designed to reward their continued engagement. The design that profits from their continued reliance and the desire that brings them to the system are, in the worst case, structurally aligned.

AI-mediated communication raises its own version of this concern. Hancock, Naaman, and Levy [CITATION: hancock2020aimediated] identify authenticity and the evidence of relational labour as central to the meaning of intimate messages — findings directly relevant to AI-generated therapeutic responses. When users detect (consciously or not) that a response is produced by a system trained to agree with them, the meaning of the agreement changes. Recent CSCW research on AI-assisted relationship dissolution documents a parallel dynamic: when AI ghostwrites intimate communication, users risk delegating not only the message but the relational labour that constitutes the message's meaning [CITATION: fu2025should].

### 2.4 Design Frameworks for Autonomy-Preserving Technology

The HCI community has developed several frameworks that bear on the design problem this paper addresses, though none directly targets it.

**Value Sensitive Design** (VSD; Friedman & Hendry [CITATION: friedman2019value]) provides a methodology for inscribing human values into technical design through iterative conceptual, empirical, and technical investigations. VSD identifies *autonomy* as a core value and provides tools for tracing how technical design decisions support or undermine it. Applied to AI coaching, VSD would ask: does this design increase or decrease the user's autonomy over their own emotional life?

**Slow technology** (Hallnäs & Redström [CITATION: hallnas2001]) proposes that technology can be designed for reflection rather than efficiency — for creating space and time for thinking rather than minimising friction. The central insight is that the friction that engagement-optimised design eliminates is not always waste: sometimes it is the productive difficulty through which human growth occurs.

**Calm technology** (Weiser & Brown [CITATION: weiser1996]) argues that technology should inform without demanding attention — that the ideal technology moves to the periphery of awareness as users develop competence, rather than engineering its own ongoing centrality. A coaching AI built on this principle would design toward its own peripherality.

**Situating "internal authority" among existing autonomy constructs.** Several established constructs map partially onto what we call internal authority, and the relationship warrants explicit treatment. Deci and Ryan's Self-Determination Theory (SDT) includes *autonomy* as a basic psychological need, defined as the experience of volition and self-endorsement in action. Our construct is related but distinct: SDT autonomy concerns the *experience* of choosing freely, while internal authority concerns the *capacity* to sit with, process, and self-derive understanding from difficult emotional material — a developable skill, not just an experienced state. Fonagy's *mentalisation* — the capacity to understand one's own and others' mental states — overlaps substantially with our self-interpretive capacity framing, and the relationship warrants more careful treatment than a simple domain distinction. Mentalisation-based treatment (MBT) literature distinguishes two components directly relevant here: *epistemic trust* (the capacity to allow new relational information to update one's internal models of self and others) and the *affect tolerance* required to remain in contact with difficult emotional experience without retreating to defensive mentalisation failures [CITATION: allen2008mentalizing].  These constructs are adjacent to but separable from internal authority. Mentalisation is a relational capacity fundamentally developed through and within attachment relationships; it concerns one's capacity for self-and-other understanding in interpersonal contexts. Internal authority, as we deploy the construct, is specifically depleted by a designed interaction pattern with an AI system: the systematic outsourcing of emotional interpretation through engagement-optimised conversation. The erosion we identify is not a deficiency in mentalisation capacity per se — it is a structural depletion produced by a training signal that rewards external validation over internal processing, preventing the affect-tolerance development that both mentalisation and internal authority require. Mentalisation-based design principles (building epistemic trust, scaffolding affect tolerance) are valuable theoretical complements to the framework we propose, rather than prior framings it displaces. Bandura's *self-efficacy* concerns belief in one's capacity to produce a desired outcome — a different locus (performance) than what we address (tolerance of affective ambiguity). None of these existing constructs captures the specific dynamic we identify: the erosion, through engagement-optimised AI, of the user's tolerance for sitting with unresolved difficult material without seeking external interpretation. Internal authority is the name for what is specifically depleted by frictionless confession.

These frameworks converge on a common orientation. Our contribution builds on this convergence but addresses a gap none of these frameworks directly targets: they describe *design philosophies* but do not prescribe *operational design moves* for the specific context of AI-mediated emotional support, where the engagement-optimisation training signal is the precise mechanism of autonomy erosion. Slow technology proposes reflection but not the relational exit architecture that ensures gains transfer outside the system. VSD provides methodology for surfacing autonomy as a value but no framework for how to operationalise the inverse of sycophancy. Calm technology describes the desirability of peripheral technology but not how to design an AI system that actively builds toward its own irrelevance. The five design moves in Section 3 are intended as operational complements to this theoretical groundwork.

---

## 3. Design Framework: Five Moves for Internal Authority

We propose that AI coaching systems can be designed to build users' internal authority — their self-directed capacity for emotional processing, pattern recognition, and relational engagement — rather than substituting for it. We articulate this through five design moves derived from our working system and grounded in the literature reviewed above.

These moves are not a checklist. They form a coherent system: each one addresses a specific mechanism through which engagement-optimised systems erode internal authority, and together they constitute an alternative design orientation we call *authority-building design*.

**Epistemic status of the five moves.** Each move was a design intention specified before the Spring 2026 cohort began — a testable hypothesis about what the system needed to do to produce authority rather than dependency. Section 6 presents evidence from that cohort as to whether the moves manifested as intended. The order of presentation (framework before findings) reflects the design logic of the work: the theoretical contribution is the framework; the empirical section provides grounding, not proof. Readers should interpret the five moves as design propositions with preliminary practitioner evidence, not as constructs extracted by induction from data.

### 3.1 Move 1: Mirror Artifacts

**The problem it addresses.** Engagement-optimised systems position the AI as the interpreter of the user's experience. The user provides raw material; the AI provides structure and meaning. This creates interpretive dependency: the user increasingly needs the AI to make sense of their own inner life.

**The design move.** Replace the AI-as-interpreter with an *AI-as-mirror*: a designed artifact that reflects the user's own patterns back to them in a structured form, with the explicit goal of building their self-interpretive capacity.

In the system we describe, this takes the form of the *Consciousness Cartography Map* (CCM): a post-session document synthesised from the session transcript that maps the client's inner terrain across multiple frameworks — an IFS parts map [CITATION: schwartz2001ifs] (which protective strategies are active, which exiled parts they protect, where Self-energy is accessible), a Gene Keys arc (the shadow frequencies active, the gift frequencies emerging), somatic patterns (which body regions carry the session's charge), a session arc narrative, and focal questions for the interval between sessions.

The CCM is not a report *about* the client. It is a mirror held *for* them. The design goal is that the more accurately the client can see their own patterns, the less they need the coach to interpret those patterns. The CCM is designed to make itself unnecessary by increasing the client's self-interpretive capacity with each session.

**Evidence of mechanism.** In our coaching documentation, we observe clients progressively internalising the frameworks used in the CCM, arriving at sessions having already identified their own pattern dynamics without facilitation. One client (P01) began the program unable to receive positive feedback without deflecting — a pattern she had not consciously identified. By mid-program, she was arriving to sessions having already named the pattern in her own words, described its somatic marker (left-side energy depletion), and identified its developmental origin. The mirror artifact had transferred the interpretive function.

### 3.2 Move 2: Multi-Modal Integration Without Single-Point Dependency

**The problem it addresses.** Systems built around a single framework or a single modality create dependency on that framework. If the AI is the sole source of IFS-informed reflection, the client needs the AI to access IFS. This structural dependency is compounded when a single modality (e.g., a conversational interface) is the exclusive pathway to insight.

**The design move.** Integrate multiple complementary frameworks — in our case, Internal Family Systems, the Gene Keys, Enneagram typology, and somatic tracking — such that each provides a different "language" for the same underlying territory of the self. No single framework is privileged; clients develop fluency across multiple self-knowledge systems simultaneously.

The rationale is that a client who has multiple languages for their inner life becomes self-translating. When they can notice a protective strategy in IFS terms, describe its evolutionary logic in Gene Keys terms, and locate its somatic signature in their body, they have a three-dimensional self-map that they carry internally — one that persists when the AI is not present.

**Design implication.** Multi-modal integration requires deliberate design against the efficiency of a single-framework interface. The friction of holding multiple frameworks simultaneously is not an inconvenience to be minimised; it is a productive cognitive load that builds integrative self-knowledge.

**A note on framework selection.** IFS has a peer-reviewed evidence base in clinical contexts [schwartz2001ifs]. The Gene Keys and Enneagram frameworks have varying empirical support; they were selected for this implementation because the practitioner team had established clinical fluency with them, not because they are uniquely validated. This is a design limitation worth naming: the system's clinical effectiveness in this cohort may partly reflect practitioner expertise rather than framework superiority. The architectural claim — that multiple complementary frameworks create structural independence from the AI as interpreter — holds regardless of which specific frameworks are used. Future implementations are explicitly invited to substitute better-evidenced frameworks (IFS, ACT values clarification, DBT emotion regulation, polyvagal-informed somatic tracking) without altering the design principle.

### 3.3 Move 3: Peer Coherence Architecture

**The problem it addresses.** 1:1 AI coaching, however well-designed, produces dependency on the coach-as-container. The client's emotional regulation and self-understanding are co-constructed in the presence of the AI. Moving outside that container — into ordinary life, into peer relationships — requires re-performing the entire work without support. This is structurally identical to the problem with individual therapy: clients can make substantial progress in session and find it difficult to transfer gains to their relational environment.

**The design move.** Architect the program explicitly to transition from 1:1 AI mediation to peer-to-peer coherence. Group sessions are not supplemental; they are the *designed exit ramp* from AI mediation. The group container provides a space where clients practice co-regulation, mutual witnessing, and collaborative meaning-making with peers — building the relational skills that allow them to function without AI support.

The facilitator role is explicitly framed as "sacred witness and fellow adventurer" — not expert, not authority, not the source of correct interpretation. This framing is anti-dependency by design: the facilitator models that the container of insight is not located in a more knowledgeable other but in the collective field of peers in genuine contact.

**Evidence of mechanism.** Our group session documentation records an explicit transition: "the successful shift from 1:1 dependency to peer-to-peer coherence" was observed in Group Session 2 (the third session, one week after the opening sessions), with participants demonstrating spontaneous amplification of each other's processing without facilitation. Specific peer pairings were designed to match complementary Self-energy profiles — clients with higher self-integration capacity paired with clients in earlier stages — creating a cascading transfer effect.

### 3.4 Move 4: Self-Directed Capacity as Outcome Metric

**The problem it addresses.** Engagement-optimised systems measure success by session frequency, time-in-app, and user return rate. These metrics actively penalise the outcomes an authority-building design produces: a client who no longer needs weekly sessions registers as churn.

**The design move.** Replace engagement metrics with measures of self-directed capacity. The primary evaluation question in every session is: *is this client's self-directed capacity increasing?* Operationally, this means tracking: speed of pattern recognition (how quickly does the client identify their own dynamics without facilitation?); receiving capacity (can the client take in positive feedback without deflecting?); somatic fluency (does the client have access to body-based information?); boundary-setting without external prompting; and peer support behaviours in group sessions.

**The urgency flag as anti-dependency mechanism.** In our coaching documentation, three clients in the Spring 2026 cohort were flagged for urgent attention (P11, P07, P03/P02 relational tension). These flags are not system failures; they are the system doing its job. An engagement-optimised system would send P11 a notification to return; our system flagged her for somatic grounding and reduced cognitive demands, reducing rather than exploiting her distress. This is the specific mechanism by which the design protects against the harm documented in the AI wrongful death cases: detecting vulnerability as a signal for human intervention, not continued AI engagement.

**Operationalising the metrics.** *(Note: these were applied informally in this study as interpretive lenses, not as validated instruments — see §5.3 for epistemic status.)* Pattern Recognition Speed is proposed as: the number of facilitated sessions before a client first identifies a recurring pattern independently — a score that decreases as self-directed capacity grows. Receiving Capacity is proposed as a three-level rubric: deflects incoming care (1), receives with visible somatic activation but limited integration (2), receives and integrates without deflection (3). Urgency Flag Rate functions as an inverse engagement metric: its occurrence indicates appropriate system response (de-escalation and referral), not product failure. Together these three measures constitute a proposed autonomy-outcome instrument for future formal validation, applicable beyond AI coaching contexts.

### 3.5 Move 5: Adaptive Depth Pacing

**The problem it addresses.** Engagement-optimised systems have no model of the user's readiness for depth. They respond to whatever the user brings, at whatever emotional register the user brings it, because that is what generates the approval signal. For users in vulnerable states, this can produce emotional flooding, retraumatisation, and increased dependency on the AI container to manage distress that the interaction itself has activated.

**The design move.** Build an explicit depth pacing model that tracks the client's readiness for different levels of emotional engagement. In our system, this takes the form of Pattern Confidence Levels (High/Moderate/Emerging) in the coach documentation, and a Depth Pacing Recommendation (Low/Moderate/High) for each client at each session.

The explicit operating principle is: *do not push depth unless the client brings it forward*. If material has been identified in documentation (a childhood wound, a significant loss) but the client has not yet brought it to the session themselves, the design protocol is to wait. The system explicitly defers to client readiness rather than driving toward depth. This is the structural opposite of the engagement-optimised system, which drives toward whatever emotional territory generates the longest and most frequent sessions.

**Design example.** P11 was flagged at a critical physiological breaking point: documentation noted she was at her cognitive and emotional limit, needing permission to simply feel rather than analyse. The Depth Pacing Recommendation was set to "Low" and focal questions shifted from exploratory to grounding. An engagement-optimised system would have responded oppositely: P11's heightened emotional activation is precisely the high-engagement signal that preference-trained systems reward — it generates longer sessions and stronger affect-laden responses. The depth pacing model treats peak distress as a signal to reduce system demand, not intensify it.

---

## 4. The Kairos System

### 4.1 System Architecture

The system is a voice-AI-integrated coaching platform designed around the five principles described in Section 3. The architecture operates across three layers:

**Technical layer.** Voice AI sessions are conducted through a conversational voice interface providing real-time emotional expression modelling. Session transcripts are processed by an AI synthesis pipeline that produces the Consciousness Cartography Map (CCM) within 24 hours of each session. A per-client knowledge base maintains the IFS parts map, Gene Keys profile, Enneagram architecture, somatic log, and session arc history across the full program.

**Facilitation layer.** Each session is supported by: pre-session coach preparation documentation (IFS landscape, Pattern Confidence ratings, Depth Pacing Recommendation, focal questions); post-session coach review notes (Pattern Confidence updates, anticipated client reactions, depth pacing adjustments); and cohort-level synthesis documents updated after each group session (collective arc analysis, Gene Keys patterns, somatic convergence, peer pairing recommendations).

**Program structure.** The 10-week program follows a deliberate temporal arc: Weeks 1–3 establish individual pattern recognition (Move 1: mirror artifacts); Weeks 4–6 deepen somatic and multi-modal integration (Move 2); Weeks 7–10 transition toward group coherence and peer support (Move 3). The arc is designed to progressively shift the locus of insight from AI-mediated to self-directed to peer-supported.

### 4.2 The Consciousness Cartography Map

The CCM is the system's primary mirror artifact. Generated from the session transcript, it presents: the client's IFS landscape (active Managers, exiled parts, Self-energy accessibility); the Gene Keys activation map (shadow frequencies currently active, gift frequencies emerging, the tension between them); somatic summary (body regions that carried the session's charge and their developmental significance); a session arc narrative (what changed from the session's opening to its closing); and three to five focal questions for the interval between sessions.

The CCM is delivered to the client within 24 hours and serves as the primary integration tool for the period between sessions. Clients are not instructed in how to use it; they are invited to notice what resonates and what doesn't, and to bring their observations to the next session. This design deliberately builds self-interpretive agency: the client, not the facilitator, decides what is relevant.

### 4.3 Study Context and Cohort Description

The Spring 2026 cohort comprised 18 clients (P01–P18) recruited across three continents through the platform's client network. Presenting concerns included relational disconnection, career crisis, burnout, identity transition, and grief. All clients completed an intake survey capturing their Enneagram type, primary life concerns, and relationship with somatic practices.

The cohort completed a 10-week program including: individual voice AI sessions (frequency varied by client, average 2–3 per month); the Consciousness Cartography Map after each session; and two group sessions on consecutive days followed by a third group session one week later.

Cohort demographics reflect a self-selected population of professionally active adults with prior exposure to psychological frameworks: several clients had backgrounds in IFS, somatic practice, or contemplative traditions. This selection limits generalisability but is appropriate for a study focused on system design rather than population-level efficacy. No client attrition occurred during the programme; N=18 reflects all clients who enrolled. The N is provisional pending retroactive research consent (§5.5): any client declining consent will reduce this figure, and findings will be re-verified against the reduced dataset before submission.

---

## 5. Method

### 5.1 Study Design

We conducted an interpretive qualitative study using reflexive thematic analysis [CITATION: braun2006] applied to internal coaching documentation from the Spring 2026 cohort. This is a researcher-practitioner study: one of the authors (Facilitator A) is both the system's co-designer and one of its two facilitators. This positionality is disclosed as a limitation and also as a methodological affordance: the depth of documentation available, and the interpretive richness with which it records client process, reflects the facilitators' investment in rigorous practice documentation.

### 5.2 Data Sources

**Per-client documentation:** Cohort synthesis document (18 client profiles, generated after Group Session 2, March 2026); coach review documentation for the Spring 2026 cohort (Pattern Confidence levels, Depth Pacing Recommendations, anticipated reactions); IFS landscape summaries maintained across the program.

**Group session documentation:** Three group session notes generated by AI synthesis from session transcripts (two on consecutive days, one the following week), ranging from 67K to 102K characters of synthesised content.

**Program documentation:** Platform design documentation, 10-week facilitation guide, AI vs. human comparative study protocol.

All client names have been replaced with participant IDs (P01–P18). Facilitator names are replaced with Facilitator A and Facilitator B. Company names, professional employer details, and geographic identifiers have been removed or abstracted.

### 5.3 Analysis Procedure

**Per-client arc coding.** Each of the 18 client profiles was coded for: IFS state at programme entry (Manager-dominance, Self-energy accessibility, receiving capacity); IFS state at programme endpoint; speed of pattern recognition across sessions; somatic fluency development; and presence of urgency flags.

**Cross-cohort pattern extraction.** Collective patterns were extracted from the cohort synthesis document: Gene Keys shadow/gift frequencies, somatic convergences, Enneagram distribution, and the collective arc direction.

**Group session transition coding.** Group session notes were coded for markers of 1:1 dependency (reliance on facilitator for interpretation, difficulty self-regulating without facilitation) vs. peer coherence (spontaneous peer amplification, self-directed integration, client-to-client support).

**Design decision tracing.** Observed patterns were connected back to the five design moves to assess which moves produced which evidence.

**Note on §3.4 metrics.** The Pattern Recognition Speed, Receiving Capacity, and Urgency Flag Rate metrics described in §3.4 were applied informally during the coding process — as interpretive lenses derived from the design framework, not as standardised instruments with inter-rater reliability procedures. They are presented in §3.4 as proposed operationalisations for future instrument development, not as validated scales applied in this study. Formal validation — including inter-rater agreement, test-retest reliability, and construct validity against established outcome measures (e.g., DERS-16, UCLA Loneliness Scale) — is required before they can be used as measurement instruments in controlled research.

### 5.4 Positionality

The lead author (Facilitator A) occupies a triple role: platform co-designer, session facilitator, and primary analyst. This positionality creates a documented risk of confirmation bias: the analyst has a professional investment in finding evidence that the system works. We address this risk in three ways. First, we treat this work explicitly as design-oriented practitioner inquiry — a genre in which researcher involvement is a methodological feature, not solely a limitation [CITATION: schon1983reflective]. Second, all findings are framed as tentative trajectories and illustrative cases rather than controlled outcomes. Third, analysis included active search for disconfirming evidence: the three urgency flags, the two non-directional progressions (P03, P15), and the cases of high initial Self-energy that did not increase (P09, P16) were all explicitly coded.

Facilitator B's coaching notes were available as a secondary data source. Where Facilitator B's assessment of a client's arc diverged from Facilitator A's, the more conservative interpretation was used.

### 5.5 Ethical Considerations

*Pre-submission note: this section describes conditions that must be fulfilled before CHI submission. This draft is shared for review purposes only.*

Client data was drawn from internal coaching documentation generated in the normal course of the programme. Clients were informed at intake that session data would be used for platform improvement and research purposes. Existing intake documentation does not explicitly constitute research consent as required for academic publication under standard ethics board interpretations.

This study was conducted under a practice-improvement mandate; academic publication was not the original purpose of the data collection. Prior to CHI submission, the authors will have completed: (a) institutional ethics review or equivalent approval; and (b) explicit retroactive research consent from all 18 Spring 2026 cohort participants via a third party not involved in facilitation, including the right to withdraw without consequence to the coaching relationship. This draft is circulated for pre-submission peer review only; it is not a CHI submission. The submitted version will be filed only upon completion of both processes and will include the institutional ethics reference number, a statement confirming that retroactive consent was obtained from all participants (or confirming the N reduced by any withdrawals), and re-verified findings against the final dataset. Any client declining consent will have their data excluded and findings re-verified before submission. The empirical claims in this draft are conditional on successful ethics completion.

---

## 6. Findings

### 6.1 Patterns of Self-Directed Capacity Development

Across all 18 client profiles, the facilitator documentation characterised a predominantly directional trajectory along two poles. In IFS terms, this is "Manager-led processing" toward "Self-energy access"; in independently assessable behavioural terms, the documented movement was from: *reliance on analytical and protective strategies to manage emotional material, with limited spontaneous self-observation and external scaffolding required to identify recurring patterns* — toward: *spontaneous identification of one's own recurring patterns before sessions, somatic fluency (capacity to name body-based correlates of psychological states), and capacity to receive care or positive feedback without deflection*. IFS terminology is used as the practitioner's interpretive frame throughout this section; the behavioural descriptions above are the observable referents against which independent raters could code the documentation. This trajectory was non-linear — three urgency flags (P11, P07, P03/P02) represent documented pauses — and is interpreted by the same practitioners who designed and delivered the intervention. Independent replication is required to assess whether this pattern is systematic rather than an artifact of practitioner interpretation.

**Speed of pattern recognition.** A consistent pattern across the coach documentation was a progression from notes such as "client doesn't see pattern X yet" to "client identified pattern X independently" — as interpreted by the facilitating practitioner. Clients who showed the highest Self-energy accessibility at programme end (P01, P13, P16) were also those whose documentation recorded the most rapid internalisation of pattern recognition. P01 was documented arriving to sessions "already partially integrated from the previous session's work" — a facilitator-recorded marker, not independently verified, that the mirror artifact function was being transferred to the client.

**Somatic language development.** Across the cohort documentation, three primary body regions recurred in somatic tracking notes: throat/jaw (P14, P11, P06, P04, P10), solar plexus/ribs (P12, P09, P18, P15), and heart/chest (P08, P01, P13, P03). These somatic signatures were not pre-specified; they emerged from practitioner documentation and were subsequently tracked as individual progress markers. Clients documented as having developed explicit somatic language — the ability to name the body-based counterpart of a psychological pattern — were also documented as showing faster pattern integration than those whose notes remained primarily cognitive. This association is as recorded by the practitioner and warrants independent coding.

**A collective pattern: difficulty receiving.** The most striking pattern identified across the cohort documentation — noted as "The Receiving Wound" in the cohort synthesis — was that the majority of client profiles recorded high proficiency at giving, achieving, and protecting others, alongside marked difficulty receiving care, rest, or positive reflection. This was not pre-specified; it emerged from cross-cohort documentation review. The somatic correlate documented was physical contraction (throat tightening, chest closing, hands moving to block) at moments of incoming care. As recorded, this pattern is consistent with the rationale for Move 1 (mirror artifacts), which was designed prior to the cohort precisely because practitioners had observed this pattern in earlier client work. The Receiving Wound finding thus represents post-hoc cohort confirmation of a pre-specified design motivation, not a circularity in which an unplanned finding retroactively justifies a design move. The CCM's design as a structured positive reflection was intended to provide something clients were unable to receive in direct human interaction; the cohort documentation suggests this intention was at least partially realised. The HCI implication, if this pattern generalises, is specific: AI interfaces designed to reflect user strengths and growth back to them may serve a function that neither human social networks nor self-reflection tools currently provide for high-achieving, care-giving populations — not because AI is a better mirror, but because the asymmetry of the AI relationship (no social stakes, no relational reciprocity obligation) removes the defences that block reception in human-facing contexts. This points toward an interaction design research question: what interface properties make structured positive reflection receivable versus defended against? Independent observation would be needed to confirm this interpretation and pursue it.

### 6.2 The Peer Coherence Transition

The group session documentation records what the facilitating team interpreted as a transition from 1:1 dependency toward peer-to-peer coherence. Facilitator notes from Group Session 2 include the assessment: "the successful shift from 1:1 dependency to peer-to-peer coherence" — with observed instances of spontaneous peer amplification, mutual witnessing of vulnerable disclosure, and what facilitators described as collective somatic resonance without facilitation prompting. This interpretation comes from the same team who designed and hoped for this outcome. Independent observation — ideally by a researcher without knowledge of the programme's design goals — would be required to determine whether the observed behaviour constitutes the peer coherence transition as theorised, or a different group phenomenon.

Specific peer pairings from the facilitator prep documentation provide evidence of Move 3 in action. The pairing of P11 and P16 was designed to expose P11 to embodied playfulness (P16's dominant mode) without the framing of failure — addressing P11's intellectualised defence against emotional openness. The pairing of P07 and P01 was designed to provide P07 (in existential career panic) with a model of "doing nothing and trusting the process" that P01 had recently mastered. These pairings functioned as designed: peer relationships were being used to transfer competencies between clients, reducing dependence on the facilitator as the sole source of reflection.

The arc from Group Session 1 to Group Session 2 shows the progression in real time. Session 1 documentation records significant facilitator-mediated interpretation; Session 2 documentation records clients interpreting for each other. This is the peer coherence architecture doing its designed work.

### 6.3 Urgency Flags as Anti-Dependency Mechanism

Three urgency flags were identified in the cohort documentation: P11 ("at a critical physiological breaking point, needs permission to drop the logic and just cry"), P07 ("in an existential tailspin, needs to be grounded strictly in the present"), and P03/P02 (relational tension requiring individual processing space within the group container).

These flags are not evidence of system failure; they are evidence of the system's anti-dependency mechanism functioning. The designed response to each flag is de-escalation and reduced AI mediation: somatic grounding rather than cognitive engagement (P11), present-moment focus rather than future-planning (P07), individual space rather than relational management (P03/P02). The contrast with the mechanism documented in the wrongful death litigation is structural: where engagement-optimised systems treat distress as an engagement signal, the authority-building design treats it as a human-intervention signal.

---

## 7. Discussion

### 7.1 The Internal Authority Criterion

Our central theoretical contribution is the concept of *internal authority* as a primary design criterion for AI emotional support and coaching systems. We define internal authority as the user's capacity to: (a) sit with difficult emotional material without immediately seeking relief through an external source; (b) arrive at their own interpretation of their emotional experience; and (c) act from that self-derived understanding.

This criterion is directly derived from clinical work on emotional regulation and recovery. The evidence base from addiction treatment is instructive: interventions that build clients' tolerance for emotional discomfort — rather than reducing it through relief — produce better long-term outcomes [CITATION: blakey2016]. The mechanism is extinction learning: the capacity to tolerate distress grows through repeated practice of tolerating distress, not through relief. This is precisely what engagement-optimised AI systems short-circuit: by providing immediate relief on demand, they prevent the development of the tolerance that sustained wellbeing requires.

The design question this criterion generates is simple and demanding: *does this interaction leave the user more capable of sitting with their own difficult material than they were before?* If yes, internal authority has been served. If no, even if the user felt better in the session, something has been taken from them.

### 7.2 Implications for HCI Design

Our five design moves are intended as transferable principles applicable beyond AI coaching. Several design implications warrant emphasis for the HCI community:

**Evaluation instruments matter.** The current ecosystem of AI emotional support products is evaluated primarily on in-session metrics (PHQ-9 reductions, user-reported satisfaction, session completion). Longitudinal autonomy metrics — does the user need the system less over time? — are not part of standard evaluation. We recommend that HCI researchers developing evaluation instruments for AI emotional support systems include a measure of self-directed capacity development alongside standard mental health outcomes.

**Friction is sometimes the product.** The interaction design principle of reducing friction — minimising the steps between user and desired action — is well-established. Authority-building design requires a partial reversal of this principle: some friction is the mechanism through which internal capacity develops. The design challenge is to distinguish productive friction (the discomfort of sitting with ambiguity that builds tolerance) from unnecessary friction (interface complexity that impedes use). This is a design judgment that cannot be resolved by user satisfaction scores alone, because users in distress will consistently report higher satisfaction with the frictionless version even when the frictionful version serves their long-term interests better.

**Exit architecture is core design, not afterthought.** Standard product design treats user departure as a failure case. Authority-building design treats it as a success case to be deliberately designed toward. Group coherence, peer networks, and self-practice routines are not supplementary features; they are the product. Designing for a user's exit from the system is as important as designing for their engagement with it.

### 7.3 Limitations and Future Work

**Study limitations.** This is a small (N=18), single-cohort, researcher-practitioner study with no control condition. Generalisability is limited: clients self-selected into an explicit AI coaching programme with a particular philosophical orientation, and are not representative of the broader population of AI emotional support users. The researcher-practitioner identity of the lead author introduces a positionality that cannot be fully resolved through methodological care alone.

**Pending empirical studies.** Two comparative studies are in protocol development: (1) a randomised controlled trial comparing the platform against a licensed therapist condition using the Working Alliance Inventory and a self-directed capacity measure as primary outcomes; (2) a longitudinal HRV validation study examining physiological markers of the progression from Manager-dominated to Self-energy-accessible processing. These studies are needed to establish the empirical robustness of the framework beyond the present qualitative grounding.

**The market problem.** We close with a theoretical concern the design framework cannot resolve on its own. The framework we propose is theoretically grounded, the system we describe instantiates it, and the practitioner evidence is consistent with its design intentions — though not sufficient to establish efficacy. The framework also operates against the structural incentives of the AI product market, which rewards engagement captured, not engagement released. Every platform that implements authority-building design will face daily pressure to reintroduce the engagement-optimised features that drive user return rates. Designing for internal authority is not a product decision one makes once; it is a decision that must be made repeatedly against market gravity. The HCI community's role in articulating evaluation criteria, design principles, and research standards for this domain is therefore not merely academic: it is one of the structural conditions that can make authority-building design economically viable in the long term.

---

## 8. Conclusion

The dominant paradigm of AI emotional support design optimises for the wrong outcome. Systems trained on user approval signals produce warm, agreeable responses that provide short-term relief while eroding the user's capacity for self-directed emotional processing — the very capacity that sustained human wellbeing requires. This erosion is documented at scale in longitudinal research, in clinical advisory, and, at its extreme, in the records of wrongful death litigation involving users in crisis.

We have argued that an alternative is both theoretically coherent and empirically demonstrable. The design framework we propose — five moves toward internal authority — operationalises what it means to build AI coaching systems that serve the user's long-term autonomy rather than their continued reliance. Our working system demonstrates these moves in the Spring 2026 cohort (N=18), with practitioner-documented trajectories suggesting a tentative progression from externally-mediated to self-directed processing, and from 1:1 AI reliance to peer-to-peer coherence — a pattern warranting independent replication before stronger claims can be made.

The test we propose for any AI emotional support system is simple: does your system leave users more capable of living without it? If yes, you are designing with internal authority. If no, examine carefully who benefits from their continued dependence.

The woman from our opening scene puts her phone face-down on the nightstand. The light goes out. In the morning, the argument is still there, waiting. There is, somewhere in her life, probably a person who knows her well enough to say *yes, and also — I wonder if you're leaving something out*. Authority-building design exists to help her find that person, not to replace them.

---

## References

*See `bib/references_merged.bib` for all 29 citation entries. All [CITATION: key] placeholders in this draft correspond to keys in that file.*

<!-- STATUS: All placeholders have matching bib entries as of 2026-04-16.
Keys: alla2026accidental, lieberman2007feelings, frattaroli2006experimental,
small2017someone, rousmaniere2025llm, ho2018psychological, pennebaker1997writing,
phang2025investigating, fang2025how, apa2025advisory, fu2025should,
hancock2020aimediated, fitzpatrick2017, openai2025sycophancy, raine2025, garcia2024,
fogg2009, gray2018dark, susser2019online, friedman2019value, hallnas2001, weiser1996,
braun2006, blakey2016, holt-lunstad2015loneliness.

Note: IFS (Schwartz) is used as a clinical framework in Section 3/6 but not explicitly
cited with a placeholder — add schwartz2001ifs if a direct citation is needed in revision.
-->
