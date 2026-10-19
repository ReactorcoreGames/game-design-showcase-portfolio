/*
  Reactorcore's game design articles. Rendered by articles.html; each one with a slug has its own page at
  articles/<slug>.html, built by tools/articles.py from the Google Docs export (original: the Google Doc it came from).
  summary: trimmed from the article's own "Summary:" paragraph. minutes: reading time at ~230 words/min,
  written by tools/articles.py when it builds the page.
  Shelves are rendered in the order listed here. featured: the recommended first read.
*/

window.SHELVES = [
  { id: "why", label: "Why games matter", note: "What games are for, and why most of them fall short." },
  { id: "metagame", label: "Infinite metagames", note: "Structures that let a game keep giving, instead of ending." },
  { id: "craft", label: "The craft", note: "What a game designer really does, and how to grow into one." },
  { id: "ethics", label: "Industry & ethics", note: "Competition, innovation, and how they shape what gets made." },
  { id: "beyond", label: "Beyond games", note: "Personal worldview that quietly drives the designs." }
];

const GDOC = id => "https://docs.google.com/document/d/" + id;

window.ARTICLES = [
  {
    shelf: "why", featured: true, minutes: 11,
    title: "Games Are Need Satisfiers",
    summary: "What games even are, what “fun” truly is, and how to see video games beyond the outdated notion of “time-wasting entertainment”: as something that empowers people rather than exploiting them.",
    slug: "games-are-need-satisfiers",
    original: GDOC("1JIuPw_kcbazTQX1hFxcadtWpvKi5tzdFKAS_UhCwihE")
  },
  {
    shelf: "why", minutes: 7,
    title: "Where Does Meaning or Motivation Come From In a Video Game?",
    summary: "Handmade versus procedural campaigns, and what actually makes each worth playing. We don’t do anything without a good reason, and knowing that reason is how you avoid making a game nobody plays.",
    slug: "where-does-meaning-come-from",
    original: GDOC("1AYFUbO3hmwBmdKqWFoU1ACUezfcruUkU_r-x3pQrDUA")
  },
  {
    shelf: "why", minutes: 9,
    title: "Throwaway Games Are a Band-Aid Approach",
    summary: "Why the industry is stagnant: self-limiting game structures that express the author’s ego more than they serve the player, and the definitive alternative to them.",
    slug: "throwaway-games-are-a-band-aid",
    original: GDOC("1c9wKcBRcRfTSqCB--S1Ku8srhI4WFAG3_7iQLclssh0")
  },
  {
    shelf: "why", minutes: 23,
    title: "Future Of Games, The Next Big Innovation",
    summary: "“Design technology”: the ways of thinking that will drive the next real evolution of games, and why the official industry can’t make it happen despite all its talent and resources.",
    slug: "future-of-games",
    original: GDOC("12SoeTeaHkPPd9xF9koa4G1LZdSMrX9kd4jV7LkeoZhU")
  },
  {
    shelf: "metagame", minutes: 36,
    title: "How To Set Up Pacing, Difficulty, And Progression Within An Infinite Metagame",
    summary: "The flaws of traditional metagame design that everyone has stopped questioning, and how procedural campaigns built from swappable modules (difficulty, pacing, length, starting conditions) make every playthrough feel different.",
    slug: "infinite-metagame-pacing-difficulty-progression",
    original: GDOC("1qfdoKELsKZFnnuKf1vBz0xZ28GMzNjvJnATPgpe5fr0")
  },
  {
    shelf: "metagame", minutes: 11,
    title: "How To Contextualize Narrative Within Infinite Metagames: Player-Run Services",
    summary: "A game built for infinite playability needs a story that supports it. Frame the player as someone running a service and taking jobs through it, and the endless structure makes sense.",
    slug: "player-run-services",
    original: GDOC("1MChlMPPABmEWdCfb-QRcsQcHiYoCithIXVCHAD5FgPI")
  },
  {
    shelf: "metagame", minutes: 11,
    title: "Additive vs Multiplicative Game Content And Why The Latter Is Better",
    summary: "The difference between content that adds up and content that multiplies, with a concrete, genre-agnostic system any game can adopt.",
    slug: "additive-vs-multiplicative-content",
    original: GDOC("1X46PJP9A6mNVZ4EZVNa80UCmH51aEBJ2jvXm51VBMBQ")
  },
  {
    shelf: "craft", minutes: 21,
    title: "What Really Is a Game Designer And How To Master This Skill",
    summary: "A straight answer to what a game designer actually does, what it takes to master it, and the harsh reality of how the industry dumps the designer’s workload on coders and artists.",
    slug: "what-is-a-game-designer",
    original: GDOC("1qYeWOujm45B-8S0Ib6_1VmpAfSoi6UmBtcJ8O2nA46Y")
  },
  {
    shelf: "craft", minutes: 16,
    title: "How To Get Started As A Complete Beginner In Game Development",
    summary: "Two ways in, for the total beginner and for the visionary who has never built a game, with the modding path that got me started and the realities others don’t talk about.",
    slug: "getting-started-in-game-development",
    original: GDOC("1su-KoRru0D2uiuaYyQ4Acu_o_uGY4TfV2Nx3LYYHAkU")
  },
  {
    shelf: "craft", minutes: 40,
    title: "How To Grow As A Game Designer. My Story and Biggest Epiphanies",
    summary: "When experiments that felt fulfilling started to feel hollow and aimless: how I got past that, and the epiphanies that let me see past the game itself to a greater whole.",
    slug: "how-to-grow-as-a-game-designer",
    original: GDOC("1Uc7p3GZabPU6zD24DEFf0Yu_BF8AB6_7BkHGVElCiIw")
  },
  {
    shelf: "craft", minutes: 6,
    title: "Evolution of a Game Designer According to Common Knowledge",
    summary: "A tidy 12-step “newbie to master” outline, trained on popular rather than correct knowledge, and the subtle traps hidden in it.",
    slug: "evolution-of-a-game-designer",
    original: GDOC("1WN99UKFgOvpaV5rKrm6XxGV005jEzthKMtxwMd78VnI")
  },
  {
    shelf: "craft", minutes: 13,
    title: "Scope Creep Is Not An Enemy, You're Just Incompetent and Inexperienced",
    summary: "Why the people warning about scope creep stifle innovation, why your dream game can be your first game, and the trick behind Scope Maximization.",
    slug: "scope-creep-is-not-an-enemy",
    original: GDOC("1dUnMhvgPTFoPFwaomh2T-dLzVyq59Deu_0r3MzPFXCI")
  },
  {
    shelf: "ethics", minutes: 4,
    title: "Forking Drives Innovation, Not Competition!",
    summary: "The talk that permanently changed how I see competition. If you believe competition is healthy and a normal part of life, you’ll be shocked how big a lie that is.",
    slug: "forking-drives-innovation",
    original: GDOC("1K9nu-s3mb8hqjHGBMGRPHWUutynIX_O45VIlfRX8-no")
  },
  {
    shelf: "ethics", minutes: 12,
    title: "Why I Don't Play Competitive Human Vs Human Games Anymore",
    summary: "Why I quit competitive games and competitive activities for good, and how I now design every project to avoid competition like the plague.",
    slug: "why-i-dont-play-competitive-games",
    original: GDOC("1AEL4GWYjHf8qOK0p_JG7hN2RIB0ogGXMOgNWE4psDfs")
  },
  {
    shelf: "beyond", minutes: 10,
    title: "My View On The Universe, Life And Death (Part 1)",
    summary: "Not strictly game design, but it shapes the metagames and universes of my projects: a universe that never began and never ends, and no reason for apathy about our future.",
    slug: "universe-life-and-death-1",
    original: GDOC("1mmytZ3GTENHpmYsCf74dMeJPNXCBrzIKKCXzSTLbBMw")
  },
  {
    shelf: "beyond", minutes: 9,
    title: "My View On The Universe, Life And Death (Part 2)",
    summary: "Honest guesses about the mechanics of a soul and what may come after death, how games usually handle death, and how these beliefs influence my design.",
    slug: "universe-life-and-death-2",
    original: GDOC("1x7K3maoEju4YL5KN4Av8ikxqzmlTvhmxetZgw8bt3Io")
  }
];
