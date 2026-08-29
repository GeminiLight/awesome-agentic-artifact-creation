document.documentElement.classList.add("js");

const DEFAULT_PAGE_SIZE = 25;
const PAGE_SIZE_OPTIONS = [10, 25, 50, 100];
const FALLBACK_COLOR = "#8a96a8";
const MINIATURE_SHOWCASE_INTERVAL = 3600;
const PAPER_TAG_ICONS = {
  artifact: "ph-cube",
  application: "ph-compass",
};

const ARTIFACT_VISUALS = {
  "Textual Artifacts": {
    visual: "textual",
    markup: `
      <svg viewBox="0 0 240 140" data-artifact-visual="textual" focusable="false">
        <defs>
          <linearGradient id="textual-material" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0" style="stop-color:color-mix(in srgb, white 88%, var(--paper))"></stop>
            <stop offset="0.58" style="stop-color:color-mix(in srgb, var(--card-color) 12%, var(--paper))"></stop>
            <stop offset="1" style="stop-color:color-mix(in srgb, var(--card-color) 38%, var(--surface))"></stop>
          </linearGradient>
          <radialGradient id="textual-platform">
            <stop offset="0" style="stop-color:var(--card-color);stop-opacity:.34"></stop>
            <stop offset="0.62" style="stop-color:var(--card-color);stop-opacity:.1"></stop>
            <stop offset="1" style="stop-color:var(--card-color);stop-opacity:0"></stop>
          </radialGradient>
        </defs>
        <ellipse class="miniature-platform" cx="120" cy="125" rx="74" ry="10" style="fill:url(#textual-platform)"></ellipse>
        <path class="miniature-depth" d="m66 105 10 12h80l9-12-7 18H72Z" style="fill:url(#textual-material)"></path>
        <path class="miniature-highlight" d="M81 37c17-9 45-12 66-6" style="fill:none"></path>
        <g class="miniature-detail"><circle cx="151" cy="111" r="2"></circle><path d="M78 112h68"></path></g>
        <g class="text-page text-page-back">
          <rect x="55" y="27" width="84" height="94" rx="3"></rect>
          <line x1="68" y1="48" x2="117" y2="48"></line>
          <line x1="68" y1="58" x2="126" y2="58"></line>
        </g>
        <g class="text-page text-page-middle">
          <rect x="91" y="20" width="88" height="101" rx="3"></rect>
          <line x1="105" y1="47" x2="162" y2="47"></line>
          <line x1="105" y1="57" x2="151" y2="57"></line>
          <line x1="105" y1="67" x2="162" y2="67"></line>
        </g>
        <g class="text-page text-page-front">
          <rect x="72" y="29" width="91" height="96" rx="3"></rect>
          <text x="87" y="52">Aa</text>
          <line x1="87" y1="64" x2="147" y2="64"></line>
          <line x1="87" y1="74" x2="138" y2="74"></line>
          <line x1="87" y1="84" x2="147" y2="84"></line>
          <line x1="87" y1="94" x2="128" y2="94"></line>
        </g>
      </svg>`,
  },
  "2D Visual Artifacts": {
    visual: "visual",
    markup: `
      <svg viewBox="0 0 240 140" data-artifact-visual="visual" focusable="false">
        <defs>
          <linearGradient id="visual-material" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0" style="stop-color:color-mix(in srgb, white 84%, var(--paper))"></stop>
            <stop offset="0.56" style="stop-color:color-mix(in srgb, var(--card-color) 18%, var(--paper))"></stop>
            <stop offset="1" style="stop-color:color-mix(in srgb, var(--card-color) 46%, var(--surface))"></stop>
          </linearGradient>
          <radialGradient id="visual-platform">
            <stop offset="0" style="stop-color:var(--card-color);stop-opacity:.38"></stop>
            <stop offset="0.68" style="stop-color:var(--card-color);stop-opacity:.09"></stop>
            <stop offset="1" style="stop-color:var(--card-color);stop-opacity:0"></stop>
          </radialGradient>
        </defs>
        <ellipse class="miniature-platform" cx="122" cy="125" rx="80" ry="10" style="fill:url(#visual-platform)"></ellipse>
        <path class="miniature-depth" d="m48 109 9 9h103l8-9-4 14H53Z" style="fill:url(#visual-material)"></path>
        <path class="miniature-highlight" d="M57 30h93" style="fill:none"></path>
        <g class="miniature-detail"><circle cx="55" cy="28" r="2"></circle><circle cx="63" cy="28" r="2"></circle><path d="M175 50v54"></path></g>
        <g class="visual-board visual-board-back">
          <rect x="116" y="36" width="72" height="75" rx="4"></rect>
          <rect class="visual-bar" x="131" y="79" width="8" height="19"></rect>
          <rect class="visual-bar" x="145" y="67" width="8" height="31"></rect>
          <rect class="visual-bar" x="159" y="56" width="8" height="42"></rect>
        </g>
        <g class="visual-board visual-board-front">
          <rect x="49" y="23" width="112" height="91" rx="4"></rect>
          <path class="visual-mountain" d="M66 87 86 64 100 77 119 50 145 87Z"></path>
          <circle class="visual-orbit" cx="132" cy="48" r="14"></circle>
          <path class="visual-orbit-slice" d="M132 34a14 14 0 0 1 12 21l-12-7Z"></path>
          <line x1="66" y1="98" x2="145" y2="98"></line>
        </g>
      </svg>`,
  },
  "Audio Artifacts": {
    visual: "audio",
    markup: `
      <svg viewBox="0 0 240 140" data-artifact-visual="audio" focusable="false">
        <defs>
          <linearGradient id="audio-material" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0" style="stop-color:color-mix(in srgb, white 78%, var(--paper))"></stop>
            <stop offset="0.5" style="stop-color:color-mix(in srgb, var(--card-color) 22%, var(--paper))"></stop>
            <stop offset="1" style="stop-color:color-mix(in srgb, var(--card-color) 54%, var(--surface))"></stop>
          </linearGradient>
          <radialGradient id="audio-platform">
            <stop offset="0" style="stop-color:var(--card-color);stop-opacity:.4"></stop>
            <stop offset="0.66" style="stop-color:var(--card-color);stop-opacity:.08"></stop>
            <stop offset="1" style="stop-color:var(--card-color);stop-opacity:0"></stop>
          </radialGradient>
        </defs>
        <ellipse class="miniature-platform" cx="120" cy="124" rx="82" ry="10" style="fill:url(#audio-platform)"></ellipse>
        <path class="miniature-depth" d="m43 106 8 10h142l9-10-4 17H47Z" style="fill:url(#audio-material)"></path>
        <path class="miniature-highlight" d="M48 38c12-8 29-8 40 0M108 48h82" style="fill:none"></path>
        <g class="miniature-detail"><circle cx="110" cy="51" r="2"></circle><circle cx="118" cy="51" r="2"></circle><path d="M111 98h78"></path></g>
        <g class="audio-speaker">
          <rect x="42" y="31" width="52" height="81" rx="8"></rect>
          <circle cx="68" cy="57" r="11"></circle>
          <circle class="speaker-cone" cx="68" cy="86" r="17"></circle>
          <circle cx="68" cy="86" r="6"></circle>
        </g>
        <g class="audio-player">
          <rect x="99" y="41" width="103" height="61" rx="7"></rect>
          <g class="audio-wave">
            <line x1="113" y1="69" x2="113" y2="77"></line>
            <line x1="121" y1="63" x2="121" y2="83"></line>
            <line x1="129" y1="58" x2="129" y2="88"></line>
            <line x1="137" y1="65" x2="137" y2="81"></line>
            <line x1="145" y1="54" x2="145" y2="92"></line>
            <line x1="153" y1="61" x2="153" y2="85"></line>
            <line x1="161" y1="57" x2="161" y2="89"></line>
            <line x1="169" y1="66" x2="169" y2="80"></line>
            <line x1="177" y1="61" x2="177" y2="85"></line>
            <line x1="185" y1="68" x2="185" y2="78"></line>
          </g>
          <line class="audio-track" x1="113" y1="91" x2="188" y2="91"></line>
          <circle class="audio-playhead" cx="139" cy="91" r="4"></circle>
        </g>
      </svg>`,
  },
  "Video Artifacts": {
    visual: "video",
    markup: `
      <svg viewBox="0 0 240 140" data-artifact-visual="video" focusable="false">
        <defs>
          <linearGradient id="video-material" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0" style="stop-color:color-mix(in srgb, var(--ink) 84%, var(--card-color))"></stop>
            <stop offset="0.55" style="stop-color:color-mix(in srgb, var(--ink) 62%, var(--card-color))"></stop>
            <stop offset="1" style="stop-color:color-mix(in srgb, var(--card-color) 58%, var(--surface))"></stop>
          </linearGradient>
          <radialGradient id="video-platform">
            <stop offset="0" style="stop-color:var(--card-color);stop-opacity:.42"></stop>
            <stop offset="0.68" style="stop-color:var(--card-color);stop-opacity:.09"></stop>
            <stop offset="1" style="stop-color:var(--card-color);stop-opacity:0"></stop>
          </radialGradient>
        </defs>
        <ellipse class="miniature-platform" cx="120" cy="124" rx="86" ry="10" style="fill:url(#video-platform)"></ellipse>
        <path class="miniature-depth" d="m31 98 8 10h161l9-10-4 17H35Z" style="fill:url(#video-material)"></path>
        <path class="miniature-highlight" d="M38 42h163" style="fill:none"></path>
        <g class="miniature-detail"><circle cx="48" cy="108" r="2"></circle><circle cx="56" cy="108" r="2"></circle><path d="M63 108h124"></path></g>
        <g class="video-rail">
          <rect x="31" y="38" width="178" height="65" rx="5"></rect>
          <path class="video-perf" d="M38 44h7m7 0h7m7 0h7m7 0h7m7 0h7m7 0h7m7 0h7m7 0h7m7 0h7m7 0h7m7 0h7m7 0h7M38 97h7m7 0h7m7 0h7m7 0h7m7 0h7m7 0h7m7 0h7m7 0h7m7 0h7m7 0h7m7 0h7m7 0h7m7 0h7"></path>
          <g class="video-strip">
            <rect x="42" y="51" width="46" height="39" rx="2"></rect>
            <path d="M48 83 60 68 69 77 82 60v23Z"></path>
            <rect x="97" y="51" width="46" height="39" rx="2"></rect>
            <path class="video-play" d="m115 62 14 9-14 9Z"></path>
            <rect x="152" y="51" width="46" height="39" rx="2"></rect>
            <circle cx="175" cy="67" r="7"></circle>
            <path d="M161 85c3-10 24-10 28 0"></path>
          </g>
        </g>
        <circle class="video-scrubber" cx="91" cy="113" r="5"></circle>
        <line class="video-timeline" x1="54" y1="113" x2="186" y2="113"></line>
      </svg>`,
  },
  "Spatial Artifacts": {
    visual: "spatial",
    markup: `
      <svg viewBox="0 0 240 140" data-artifact-visual="spatial" focusable="false">
        <defs>
          <linearGradient id="spatial-material" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0" style="stop-color:color-mix(in srgb, white 68%, var(--paper))"></stop>
            <stop offset="0.48" style="stop-color:color-mix(in srgb, var(--card-color) 26%, var(--paper))"></stop>
            <stop offset="1" style="stop-color:color-mix(in srgb, var(--card-color) 62%, var(--surface))"></stop>
          </linearGradient>
          <radialGradient id="spatial-platform">
            <stop offset="0" style="stop-color:var(--card-color);stop-opacity:.46"></stop>
            <stop offset="0.62" style="stop-color:var(--card-color);stop-opacity:.11"></stop>
            <stop offset="1" style="stop-color:var(--card-color);stop-opacity:0"></stop>
          </radialGradient>
        </defs>
        <ellipse class="miniature-platform" cx="120" cy="125" rx="80" ry="10" style="fill:url(#spatial-platform)"></ellipse>
        <path class="miniature-depth" d="m45 105 78 32 73-32-8 13-65 27-70-29Z" style="fill:url(#spatial-material)"></path>
        <path class="miniature-highlight" d="m83 49 38-21 39 21" style="fill:none"></path>
        <g class="miniature-detail"><circle cx="121" cy="27" r="2"></circle><circle cx="45" cy="105" r="2"></circle><circle cx="196" cy="105" r="2"></circle></g>
        <g class="spatial-grid">
          <path d="m45 105 73-42 78 42-73 32Z"></path>
          <path d="M62 95l74 33M79 85l74 35M96 75l74 35M179 95l-73 34M162 85l-74 35M145 75l-74 35"></path>
        </g>
        <g class="spatial-frame">
          <path d="m82 49 39-22 41 22-41 23Z"></path>
          <path d="M82 49v45l39 23 41-23V49M121 72v45"></path>
        </g>
        <g class="spatial-cubes">
          <g class="spatial-cube cube-a">
            <path class="cube-top" d="m105 66 14 8-14 8-14-8Z"></path>
            <path class="cube-left" d="m91 74 14 8v17l-14-8Z"></path>
            <path class="cube-right" d="m119 74-14 8v17l14-8Z"></path>
          </g>
          <g class="spatial-cube cube-b">
            <path class="cube-top" d="m136 50 13 7-13 8-13-8Z"></path>
            <path class="cube-left" d="m123 57 13 8v15l-13-8Z"></path>
            <path class="cube-right" d="m149 57-13 8v15l13-8Z"></path>
          </g>
          <g class="spatial-cube cube-c">
            <path class="cube-top" d="m143 81 12 6-12 7-11-7Z"></path>
            <path class="cube-left" d="m132 87 11 7v13l-11-6Z"></path>
            <path class="cube-right" d="m155 87-12 7v13l12-6Z"></path>
          </g>
        </g>
      </svg>`,
  },
  "Behavioral Artifacts": {
    visual: "behavioral",
    markup: `
      <svg viewBox="0 0 240 140" data-artifact-visual="behavioral" focusable="false">
        <defs>
          <linearGradient id="behavioral-material" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0" style="stop-color:color-mix(in srgb, var(--ink) 88%, var(--card-color))"></stop>
            <stop offset="0.52" style="stop-color:color-mix(in srgb, var(--ink) 66%, var(--card-color))"></stop>
            <stop offset="1" style="stop-color:color-mix(in srgb, var(--card-color) 55%, var(--surface))"></stop>
          </linearGradient>
          <radialGradient id="behavioral-platform">
            <stop offset="0" style="stop-color:var(--card-color);stop-opacity:.44"></stop>
            <stop offset="0.66" style="stop-color:var(--card-color);stop-opacity:.1"></stop>
            <stop offset="1" style="stop-color:var(--card-color);stop-opacity:0"></stop>
          </radialGradient>
        </defs>
        <ellipse class="miniature-platform" cx="120" cy="124" rx="84" ry="10" style="fill:url(#behavioral-platform)"></ellipse>
        <path class="miniature-depth" d="m28 103 10 12h161l10-12-5 20H33Z" style="fill:url(#behavioral-material)"></path>
        <path class="miniature-highlight" d="M36 31h96" style="fill:none"></path>
        <g class="miniature-detail"><circle cx="147" cy="39" r="2"></circle><circle cx="155" cy="39" r="2"></circle><path d="M146 45h54"></path></g>
        <g class="behavior-window">
          <rect x="28" y="27" width="113" height="82" rx="5"></rect>
          <line x1="28" y1="42" x2="141" y2="42"></line>
          <circle cx="38" cy="35" r="2"></circle>
          <circle cx="46" cy="35" r="2"></circle>
          <circle cx="54" cy="35" r="2"></circle>
          <path class="behavior-code" d="m48 59-8 7 8 7m19-14 8 7-8 7M61 54 54 78"></path>
          <path class="behavior-code-soft" d="M84 57h37M84 67h29M84 77h34M42 91h80"></path>
        </g>
        <g class="behavior-flow">
          <path d="M147 54h17v21h14M147 91h17V75"></path>
          <rect class="behavior-node node-a" x="164" y="43" width="24" height="20" rx="4"></rect>
          <rect class="behavior-node node-b" x="178" y="65" width="31" height="20" rx="4"></rect>
          <rect class="behavior-node node-c" x="156" y="89" width="27" height="20" rx="4"></rect>
          <circle class="behavior-pulse" cx="164" cy="75" r="3"></circle>
        </g>
      </svg>`,
  },
};

const APPLICATION_VISUALS = {
  "Creative Production": {
    visual: "creative",
    color: "#b777a7",
    descriptor: "Writing · Images · Music · Video",
    markup: `
      <svg viewBox="0 0 240 140" data-application-visual="creative" focusable="false">
        <defs>
          <linearGradient id="creative-material" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0" style="stop-color:color-mix(in srgb, white 84%, var(--paper))"></stop>
            <stop offset="0.55" style="stop-color:color-mix(in srgb, var(--card-color) 18%, var(--paper))"></stop>
            <stop offset="1" style="stop-color:color-mix(in srgb, var(--card-color) 52%, var(--surface))"></stop>
          </linearGradient>
          <radialGradient id="creative-platform">
            <stop offset="0" style="stop-color:var(--card-color);stop-opacity:.42"></stop>
            <stop offset="0.66" style="stop-color:var(--card-color);stop-opacity:.09"></stop>
            <stop offset="1" style="stop-color:var(--card-color);stop-opacity:0"></stop>
          </radialGradient>
        </defs>
        <ellipse class="miniature-platform" cx="120" cy="124" rx="80" ry="10" style="fill:url(#creative-platform)"></ellipse>
        <path class="miniature-depth" d="m45 102 9 13h130l8-13-4 21H50Z" style="fill:url(#creative-material)"></path>
        <path class="miniature-highlight" d="M52 37h91" style="fill:none"></path>
        <g class="miniature-detail"><circle cx="53" cy="36" r="2"></circle><circle cx="61" cy="36" r="2"></circle><path d="M53 104h119"></path></g>
        <g class="app-canvas">
          <rect x="45" y="31" width="106" height="77" rx="5"></rect>
          <path d="M58 91 79 68l16 16 18-27 26 34Z"></path>
          <circle cx="123" cy="50" r="8"></circle>
        </g>
        <g class="creative-tools">
          <path d="m162 39 7-15 7 15 15 7-15 7-7 15-7-15-15-7Z"></path>
          <path d="m156 81 26-18 8 8-18 26-18 5Z"></path>
          <path d="m154 102 18-5-13-13Z"></path>
        </g>
      </svg>`,
  },
  "Brand Communication": {
    visual: "brand",
    color: "#d89368",
    descriptor: "Identity · Campaigns · Storytelling",
    markup: `
      <svg viewBox="0 0 240 140" data-application-visual="brand" focusable="false">
        <defs>
          <linearGradient id="brand-material" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0" style="stop-color:color-mix(in srgb, white 76%, var(--paper))"></stop>
            <stop offset="0.5" style="stop-color:color-mix(in srgb, var(--card-color) 25%, var(--paper))"></stop>
            <stop offset="1" style="stop-color:color-mix(in srgb, var(--card-color) 58%, var(--surface))"></stop>
          </linearGradient>
          <radialGradient id="brand-platform">
            <stop offset="0" style="stop-color:var(--card-color);stop-opacity:.42"></stop>
            <stop offset="0.65" style="stop-color:var(--card-color);stop-opacity:.09"></stop>
            <stop offset="1" style="stop-color:var(--card-color);stop-opacity:0"></stop>
          </radialGradient>
        </defs>
        <ellipse class="miniature-platform" cx="120" cy="124" rx="78" ry="10" style="fill:url(#brand-platform)"></ellipse>
        <path class="miniature-depth" d="m48 92 10 18h130l8-18-4 31H54Z" style="fill:url(#brand-material)"></path>
        <path class="miniature-highlight" d="M52 65h14M64 55l47-18" style="fill:none"></path>
        <g class="miniature-detail"><circle cx="187" cy="91" r="2"></circle><circle cx="197" cy="91" r="2"></circle><path d="M154 107h51"></path></g>
        <g class="brand-megaphone">
          <path d="M58 63v24l58 21V42Z"></path>
          <rect x="45" y="60" width="24" height="30" rx="5"></rect>
          <path d="m72 89 12 31h20L92 96"></path>
        </g>
        <g class="brand-signal">
          <path d="M134 51c14 8 14 39 0 47"></path>
          <path d="M149 39c23 16 23 54 0 70"></path>
          <circle cx="184" cy="49" r="10"></circle>
          <path d="m184 39 3 7 7 3-7 3-3 7-3-7-7-3 7-3Z"></path>
        </g>
      </svg>`,
  },
  "Educational Support": {
    visual: "education",
    color: "#718dca",
    descriptor: "Teaching · Tutoring · Learning materials",
    markup: `
      <svg viewBox="0 0 240 140" data-application-visual="education" focusable="false">
        <defs>
          <linearGradient id="education-material" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0" style="stop-color:color-mix(in srgb, white 86%, var(--paper))"></stop>
            <stop offset="0.56" style="stop-color:color-mix(in srgb, var(--card-color) 16%, var(--paper))"></stop>
            <stop offset="1" style="stop-color:color-mix(in srgb, var(--card-color) 48%, var(--surface))"></stop>
          </linearGradient>
          <radialGradient id="education-platform">
            <stop offset="0" style="stop-color:var(--card-color);stop-opacity:.42"></stop>
            <stop offset="0.66" style="stop-color:var(--card-color);stop-opacity:.09"></stop>
            <stop offset="1" style="stop-color:var(--card-color);stop-opacity:0"></stop>
          </radialGradient>
        </defs>
        <ellipse class="miniature-platform" cx="120" cy="124" rx="82" ry="10" style="fill:url(#education-platform)"></ellipse>
        <path class="miniature-depth" d="m37 100 12 15h139l10-15-5 23H43Z" style="fill:url(#education-material)"></path>
        <path class="miniature-highlight" d="M44 53c22-6 42-1 60 10" style="fill:none"></path>
        <g class="miniature-detail"><circle cx="48" cy="110" r="2"></circle><circle cx="190" cy="110" r="2"></circle><path d="M56 114h126"></path></g>
        <g class="education-book">
          <path d="M37 48c31-8 55 3 72 18v52c-19-15-42-24-72-17Z"></path>
          <path d="M109 66c18-15 42-26 74-18v53c-30-7-54 2-74 17Z"></path>
          <path d="M51 62c19-2 35 3 46 12M51 75c19-2 35 3 46 12M169 62c-19-2-35 3-47 12M169 75c-19-2-35 3-47 12"></path>
        </g>
        <g class="education-cap">
          <path d="m143 30 35-16 35 16-35 17Z"></path>
          <path d="M157 38v16c12 9 31 9 43 0V38"></path>
          <path d="M211 31v28"></path>
          <circle cx="211" cy="62" r="3"></circle>
        </g>
      </svg>`,
  },
  "Professional Work": {
    visual: "professional",
    color: "#4c9d96",
    descriptor: "Documents · Decisions · Operations",
    markup: `
      <svg viewBox="0 0 240 140" data-application-visual="professional" focusable="false">
        <defs>
          <linearGradient id="professional-material" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0" style="stop-color:color-mix(in srgb, white 84%, var(--paper))"></stop>
            <stop offset="0.54" style="stop-color:color-mix(in srgb, var(--card-color) 17%, var(--paper))"></stop>
            <stop offset="1" style="stop-color:color-mix(in srgb, var(--card-color) 50%, var(--surface))"></stop>
          </linearGradient>
          <radialGradient id="professional-platform">
            <stop offset="0" style="stop-color:var(--card-color);stop-opacity:.44"></stop>
            <stop offset="0.66" style="stop-color:var(--card-color);stop-opacity:.1"></stop>
            <stop offset="1" style="stop-color:var(--card-color);stop-opacity:0"></stop>
          </radialGradient>
        </defs>
        <ellipse class="miniature-platform" cx="120" cy="124" rx="80" ry="10" style="fill:url(#professional-platform)"></ellipse>
        <path class="miniature-depth" d="m42 109 9 9h146l9-9-5 14H47Z" style="fill:url(#professional-material)"></path>
        <path class="miniature-highlight" d="M49 31h141" style="fill:none"></path>
        <g class="miniature-detail"><circle cx="174" cy="96" r="2"></circle><circle cx="183" cy="96" r="2"></circle><path d="M151 104h38"></path></g>
        <g class="professional-window">
          <rect x="42" y="25" width="155" height="91" rx="6"></rect>
          <line x1="42" y1="42" x2="197" y2="42"></line>
          <circle cx="53" cy="34" r="2"></circle><circle cx="61" cy="34" r="2"></circle><circle cx="69" cy="34" r="2"></circle>
          <rect x="57" y="56" width="47" height="8" rx="2"></rect>
          <rect x="57" y="72" width="86" height="5" rx="2"></rect>
          <rect x="57" y="84" width="70" height="5" rx="2"></rect>
          <rect x="57" y="96" width="79" height="5" rx="2"></rect>
          <path class="professional-check" d="m154 77 9 9 20-24"></path>
        </g>
      </svg>`,
  },
  "Scientific Research": {
    visual: "science",
    color: "#66add0",
    descriptor: "Discovery · Analysis · Scholarly work",
    markup: `
      <svg viewBox="0 0 240 140" data-application-visual="science" focusable="false">
        <defs>
          <linearGradient id="science-material" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0" style="stop-color:color-mix(in srgb, white 78%, var(--paper))"></stop>
            <stop offset="0.5" style="stop-color:color-mix(in srgb, var(--card-color) 22%, var(--paper))"></stop>
            <stop offset="1" style="stop-color:color-mix(in srgb, var(--card-color) 58%, var(--surface))"></stop>
          </linearGradient>
          <radialGradient id="science-platform">
            <stop offset="0" style="stop-color:var(--card-color);stop-opacity:.46"></stop>
            <stop offset="0.65" style="stop-color:var(--card-color);stop-opacity:.11"></stop>
            <stop offset="1" style="stop-color:var(--card-color);stop-opacity:0"></stop>
          </radialGradient>
        </defs>
        <ellipse class="miniature-platform" cx="120" cy="125" rx="80" ry="10" style="fill:url(#science-platform)"></ellipse>
        <path class="miniature-depth" d="m50 104 10 13h140l9-13-5 19H55Z" style="fill:url(#science-material)"></path>
        <path class="miniature-highlight" d="M152 39h30M73 25c11-4 22-4 33 0" style="fill:none"></path>
        <g class="miniature-detail"><circle cx="53" cy="106" r="2"></circle><circle cx="202" cy="106" r="2"></circle><path d="M61 113h132"></path></g>
        <g class="science-orbit">
          <ellipse cx="89" cy="64" rx="46" ry="17"></ellipse>
          <ellipse cx="89" cy="64" rx="46" ry="17" transform="rotate(60 89 64)"></ellipse>
          <ellipse cx="89" cy="64" rx="46" ry="17" transform="rotate(120 89 64)"></ellipse>
          <circle cx="89" cy="64" r="7"></circle>
          <circle class="science-electron" cx="132" cy="64" r="4"></circle>
        </g>
        <g class="science-flask">
          <path d="M163 32v29l-23 42c-5 9 1 17 12 17h48c11 0 17-8 12-17l-24-42V32"></path>
          <line x1="158" y1="32" x2="193" y2="32"></line>
          <path class="science-liquid" d="M151 93h49l12 20c-2 5-6 7-12 7h-48c-7 0-11-2-13-7Z"></path>
          <circle cx="176" cy="82" r="4"></circle><circle cx="188" cy="91" r="3"></circle>
        </g>
      </svg>`,
  },
  "Engineering Design": {
    visual: "engineering",
    color: "#9380c1",
    descriptor: "Software · Products · Built systems",
    markup: `
      <svg viewBox="0 0 240 140" data-application-visual="engineering" focusable="false">
        <defs>
          <linearGradient id="engineering-material" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0" style="stop-color:color-mix(in srgb, white 82%, var(--paper))"></stop>
            <stop offset="0.53" style="stop-color:color-mix(in srgb, var(--card-color) 19%, var(--paper))"></stop>
            <stop offset="1" style="stop-color:color-mix(in srgb, var(--card-color) 56%, var(--surface))"></stop>
          </linearGradient>
          <radialGradient id="engineering-platform">
            <stop offset="0" style="stop-color:var(--card-color);stop-opacity:.45"></stop>
            <stop offset="0.66" style="stop-color:var(--card-color);stop-opacity:.1"></stop>
            <stop offset="1" style="stop-color:var(--card-color);stop-opacity:0"></stop>
          </radialGradient>
        </defs>
        <ellipse class="miniature-platform" cx="120" cy="124" rx="82" ry="10" style="fill:url(#engineering-platform)"></ellipse>
        <path class="miniature-depth" d="m34 107 10 11h155l9-11-5 16H39Z" style="fill:url(#engineering-material)"></path>
        <path class="miniature-highlight" d="M42 35h115" style="fill:none"></path>
        <g class="miniature-detail"><circle cx="174" cy="33" r="2"></circle><circle cx="182" cy="33" r="2"></circle><path d="M170 41h37"></path></g>
        <g class="engineering-plan">
          <rect x="34" y="28" width="133" height="88" rx="4"></rect>
          <path d="M51 45h42v24H51ZM104 45h46v54h-27V81h-19ZM51 80h40v19H51Z"></path>
          <path d="M45 40h112M45 108h112"></path>
        </g>
        <g class="engineering-gear">
          <path d="m185 49 6 4 8-2 4 7-5 7 1 8-7 4-7-5-8 2-4-7 5-7-1-8Z"></path>
          <circle cx="188" cy="62" r="8"></circle>
          <path class="engineering-pencil" d="m158 95 38-38 10 10-38 38-15 5Z"></path>
        </g>
      </svg>`,
  },
};

const state = {
  catalog: null,
  view: "artifact",
  primary: "",
  year: "",
  kind: "",
  status: "",
  search: "",
  sort: "recent",
  page: 1,
  pageSize: DEFAULT_PAGE_SIZE,
};

const elements = {
  resultsPanel: document.querySelector(".results-panel"),
  paperList: document.querySelector("#paper-list"),
  resultCount: document.querySelector("#result-count"),
  emptyState: document.querySelector("#empty-state"),
  pagination: document.querySelector("#pagination"),
  search: document.querySelector("#paper-search"),
  primary: document.querySelector("#primary-filter"),
  primaryLabel: document.querySelector("#primary-filter-label"),
  year: document.querySelector("#year-filter"),
  kind: document.querySelector("#kind-filter"),
  status: document.querySelector("#status-filter"),
  sort: document.querySelector("#sort-order"),
  pageSize: document.querySelector("#page-size"),
  activeFilters: document.querySelector("#active-filters"),
  clearFilters: document.querySelector("#clear-filters"),
  filterPanel: document.querySelector(".filter-panel"),
  filterPanelToggle: document.querySelector(".filter-panel-toggle"),
  familyOverview: document.querySelector("#family-overview"),
  applicationOverview: document.querySelector("#application-overview"),
};

const selectWidgets = new WeakMap();
const selectWidgetList = [];
let selectWidgetCount = 0;

function createElement(tag, className, text) {
  const element = document.createElement(tag);
  if (className) element.className = className;
  if (text !== undefined) element.textContent = text;
  return element;
}

function createIcon(name) {
  const icon = createElement("i", `ph ${name}`);
  icon.setAttribute("aria-hidden", "true");
  return icon;
}

function titleCase(value) {
  return value ? value.charAt(0).toUpperCase() + value.slice(1) : "";
}

function formatNumber(value) {
  return new Intl.NumberFormat("en").format(value);
}

function animateCount(element, target, index) {
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reducedMotion || !Number.isFinite(target)) {
    element.textContent = formatNumber(target);
    return;
  }

  const delay = index * 80;
  const duration = 900;
  const start = performance.now() + delay;
  element.textContent = "0";

  function update(timestamp) {
    if (timestamp < start) {
      window.requestAnimationFrame(update);
      return;
    }
    const progress = Math.min((timestamp - start) / duration, 1);
    const eased = 1 - (1 - progress) ** 3;
    element.textContent = formatNumber(Math.round(target * eased));
    if (progress < 1) window.requestAnimationFrame(update);
  }

  window.requestAnimationFrame(update);
}

function closeCustomSelect(widget, { restoreFocus = false } = {}) {
  if (!widget || !widget.wrapper.classList.contains("is-open")) return;
  widget.wrapper.classList.remove("is-open");
  widget.trigger.setAttribute("aria-expanded", "false");
  widget.menu.hidden = true;
  if (restoreFocus) widget.trigger.focus();
}

function closeOtherCustomSelects(activeWidget) {
  selectWidgetList.forEach((widget) => {
    if (widget !== activeWidget) closeCustomSelect(widget);
  });
}

function customSelectOptions(widget) {
  return [...widget.menu.querySelectorAll('[role="option"]')];
}

function focusCustomSelectOption(widget, index) {
  const options = customSelectOptions(widget);
  if (!options.length) return;
  const nextIndex = Math.max(0, Math.min(index, options.length - 1));
  options[nextIndex].focus();
  options[nextIndex].scrollIntoView({ block: "nearest" });
}

function openCustomSelect(widget, preferredIndex = widget.select.selectedIndex) {
  closeOtherCustomSelects(widget);
  widget.wrapper.classList.add("is-open");
  widget.trigger.setAttribute("aria-expanded", "true");
  widget.menu.hidden = false;
  focusCustomSelectOption(widget, preferredIndex < 0 ? 0 : preferredIndex);
}

function chooseCustomSelectOption(widget, index) {
  const option = widget.select.options[index];
  if (!option || option.disabled) return;
  const changed = widget.select.selectedIndex !== index;
  widget.select.selectedIndex = index;
  refreshCustomSelect(widget.select);
  widget.trigger.focus();
  if (changed) {
    widget.select.dispatchEvent(new Event("change", { bubbles: true }));
  }
}

function handleCustomSelectKeydown(event, widget, index) {
  const lastIndex = widget.select.options.length - 1;
  if (event.key === "ArrowDown") {
    event.preventDefault();
    focusCustomSelectOption(widget, index === lastIndex ? 0 : index + 1);
  } else if (event.key === "ArrowUp") {
    event.preventDefault();
    focusCustomSelectOption(widget, index === 0 ? lastIndex : index - 1);
  } else if (event.key === "Home") {
    event.preventDefault();
    focusCustomSelectOption(widget, 0);
  } else if (event.key === "End") {
    event.preventDefault();
    focusCustomSelectOption(widget, lastIndex);
  } else if (event.key === "Enter" || event.key === " ") {
    event.preventDefault();
    chooseCustomSelectOption(widget, index);
  } else if (event.key === "Escape") {
    event.preventDefault();
    closeCustomSelect(widget, { restoreFocus: true });
  } else if (event.key === "Tab") {
    closeCustomSelect(widget);
  }
}

function refreshCustomSelect(select) {
  const widget = selectWidgets.get(select);
  if (!widget) return;

  closeCustomSelect(widget);
  const fragment = document.createDocumentFragment();
  [...select.options].forEach((option, index) => {
    const item = createElement("div", "select-option", option.textContent);
    item.id = `${widget.menu.id}-option-${index}`;
    item.dataset.index = String(index);
    item.setAttribute("role", "option");
    item.setAttribute("aria-selected", String(option.selected));
    item.tabIndex = -1;
    if (option.selected) item.classList.add("is-selected");
    if (option.disabled) item.setAttribute("aria-disabled", "true");
    item.addEventListener("click", () => chooseCustomSelectOption(widget, index));
    item.addEventListener("keydown", (event) =>
      handleCustomSelectKeydown(event, widget, index),
    );
    fragment.append(item);
  });
  widget.menu.replaceChildren(fragment);
  const selected = select.options[select.selectedIndex] || select.options[0];
  widget.value.textContent = selected ? selected.textContent : "Select";
}

function enhanceSelect(select) {
  if (selectWidgets.has(select)) return;

  selectWidgetCount += 1;
  const wrapper = createElement("div", "custom-select");
  const trigger = createElement("button", "select-trigger");
  const value = createElement("span", "select-value");
  const caret = createElement("span", "select-caret");
  const menu = createElement("div", "select-menu");
  const menuId = `select-menu-${selectWidgetCount}`;
  const labelId = select.getAttribute("aria-labelledby");

  trigger.type = "button";
  trigger.setAttribute("aria-haspopup", "listbox");
  trigger.setAttribute("aria-expanded", "false");
  trigger.setAttribute("aria-controls", menuId);
  if (labelId) trigger.setAttribute("aria-labelledby", `${labelId} ${menuId}-value`);
  value.id = `${menuId}-value`;
  caret.setAttribute("aria-hidden", "true");
  menu.id = menuId;
  menu.setAttribute("role", "listbox");
  if (labelId) menu.setAttribute("aria-labelledby", labelId);
  menu.hidden = true;

  select.classList.add("select-native-hidden");
  select.tabIndex = -1;
  select.setAttribute("aria-hidden", "true");
  const selectParent = select.parentNode;
  selectParent.insertBefore(wrapper, select);
  wrapper.append(select, trigger, menu);
  trigger.append(value, caret);

  const widget = { select, wrapper, trigger, value, menu };
  selectWidgets.set(select, widget);
  selectWidgetList.push(widget);
  refreshCustomSelect(select);

  trigger.addEventListener("click", () => {
    if (wrapper.classList.contains("is-open")) {
      closeCustomSelect(widget);
    } else {
      openCustomSelect(widget);
    }
  });
  trigger.addEventListener("keydown", (event) => {
    if (["ArrowDown", "ArrowUp", "Enter", " "].includes(event.key)) {
      event.preventDefault();
      const preferredIndex =
        event.key === "ArrowUp" ? select.options.length - 1 : select.selectedIndex;
      openCustomSelect(widget, preferredIndex);
    } else if (event.key === "Escape") {
      closeCustomSelect(widget);
    }
  });
}

function setupCustomSelects() {
  [
    elements.primary,
    elements.year,
    elements.kind,
    elements.status,
    elements.pageSize,
    elements.sort,
  ].forEach(enhanceSelect);
  document.addEventListener("pointerdown", (event) => {
    selectWidgetList.forEach((widget) => {
      if (!widget.wrapper.contains(event.target)) closeCustomSelect(widget);
    });
  });
}

function familyColor(paper) {
  const family = state.catalog.families.find(
    (candidate) => candidate.name === paper.artifact_family,
  );
  return family ? family.color : FALLBACK_COLOR;
}

function setSelectOptions(select, options, emptyLabel) {
  select.replaceChildren();
  const empty = new Option(emptyLabel, "");
  select.add(empty);
  options.forEach(({ label, value }) => select.add(new Option(label, value)));
  refreshCustomSelect(select);
}

function hydrateSummary() {
  const { summary } = state.catalog;
  document.querySelectorAll("[data-stat]").forEach((element, index) => {
    const value = summary[element.dataset.stat];
    if (element.hasAttribute("data-count-up")) {
      animateCount(element, value, index);
    } else {
      element.textContent = formatNumber(value);
    }
  });
}

function createArtifactMiniature(config) {
  const miniature = createElement("span", "artifact-miniature");
  miniature.setAttribute("aria-hidden", "true");
  miniature.innerHTML = config.markup;
  return miniature;
}

function createApplicationMiniature(config) {
  const miniature = createElement("span", "application-miniature");
  miniature.setAttribute("aria-hidden", "true");
  miniature.innerHTML = config.markup;
  return miniature;
}

function createGalleryCardCopy(title, description, swatch = false) {
  const copy = createElement("span", "taxonomy-card-copy");
  const heading = createElement("span", "taxonomy-card-heading");
  if (swatch) heading.append(createElement("span", "taxonomy-swatch"));
  heading.append(createElement("strong", "", title));
  copy.append(heading, createElement("span", "taxonomy-types", description));
  return copy;
}

function renderTaxonomyOverview() {
  const familyFragment = document.createDocumentFragment();
  state.catalog.families.forEach((family, index) => {
    const visual = ARTIFACT_VISUALS[family.name];
    const button = createElement("button", "taxonomy-item taxonomy-card");
    button.type = "button";
    button.style.setProperty("--family-color", family.color);
    button.style.setProperty("--card-color", family.color);
    button.style.setProperty("--item-delay", `${index * 45}ms`);
    button.setAttribute("aria-label", `Browse ${family.name}`);
    button.dataset.artifactVisual = visual.visual;

    button.append(
      createArtifactMiniature(visual),
      createGalleryCardCopy(
        family.name,
        family.types
          .filter((type) => type.count)
          .map((type) => type.name)
          .join(" · "),
        true,
      ),
    );
    button.append(
      createElement("span", "taxonomy-count", `${family.count} papers`),
      createIcon("ph-arrow-up-right"),
    );
    button.addEventListener("click", () => openCatalog("artifact", family.name));
    familyFragment.append(button);
  });
  elements.familyOverview.replaceChildren(familyFragment);

  const applicationFragment = document.createDocumentFragment();
  state.catalog.applications.forEach((application, index) => {
    const visual = APPLICATION_VISUALS[application.name];
    const button = createElement("button", "application-item application-card");
    button.type = "button";
    button.style.setProperty("--card-color", visual.color);
    button.style.setProperty("--item-delay", `${index * 45}ms`);
    button.setAttribute("aria-label", `Browse ${application.name}`);
    button.dataset.applicationVisual = visual.visual;
    button.append(
      createApplicationMiniature(visual),
      createGalleryCardCopy(application.name, visual.descriptor),
    );
    button.append(
      createElement("span", "application-count", `${application.count} papers`),
      createIcon("ph-arrow-up-right"),
    );
    button.addEventListener("click", () => openCatalog("application", application.name));
    applicationFragment.append(button);
  });
  elements.applicationOverview.replaceChildren(applicationFragment);
}

function renderFilterOptions() {
  const options =
    state.view === "artifact"
      ? state.catalog.families.map((family) => ({
          label: `${family.name} (${family.count})`,
          value: family.name,
        }))
      : state.catalog.applications.map((application) => ({
          label: `${application.name} (${application.count})`,
          value: application.name,
        }));

  const noneLabel =
    state.view === "artifact" ? "No artifact label" : "No application label";
  const emptyLabel = state.view === "artifact" ? "All families" : "All domains";
  options.push({ label: noneLabel, value: "__none__" });
  setSelectOptions(elements.primary, options, emptyLabel);
  elements.primary.value = state.primary;
  refreshCustomSelect(elements.primary);
  elements.primaryLabel.textContent =
    state.view === "artifact" ? "Artifact family" : "Application domain";

  document.querySelectorAll('input[name="catalog-view"]').forEach((input) => {
    input.checked = input.value === state.view;
  });
}

function renderYearOptions() {
  setSelectOptions(
    elements.year,
    state.catalog.years.map(({ year, count }) => ({
      label: `${year} (${count})`,
      value: year,
    })),
    "All years",
  );
  elements.year.value = state.year;
  refreshCustomSelect(elements.year);
}

function searchableText(paper) {
  return [
    paper.title,
    paper.name,
    paper.authors,
    paper.venue_display_name,
    paper.artifact_family,
    paper.artifact_type,
    paper.artifact_subtype,
    paper.application_domain,
    paper.application_subdomain,
  ]
    .join(" ")
    .toLocaleLowerCase();
}

function filteredPapers() {
  const primaryField =
    state.view === "artifact" ? "artifact_family" : "application_domain";
  const queryTerms = state.search
    .trim()
    .toLocaleLowerCase()
    .split(/\s+/)
    .filter(Boolean);

  const papers = state.catalog.papers.filter((paper) => {
    const primaryMatches =
      !state.primary ||
      (state.primary === "__none__"
        ? !paper[primaryField]
        : paper[primaryField] === state.primary);
    return (
      primaryMatches &&
      (!state.year || paper.year === state.year) &&
      (!state.kind || paper.entry_kind === state.kind) &&
      (!state.status || paper.type === state.status) &&
      (!queryTerms.length ||
        queryTerms.every((term) => searchableText(paper).includes(term)))
    );
  });

  return papers.sort((left, right) => {
    if (state.sort === "title") {
      return left.title.localeCompare(right.title);
    }
    return (
      Number(right.year) - Number(left.year) ||
      left.venue_display_name.localeCompare(right.venue_display_name) ||
      left.title.localeCompare(right.title)
    );
  });
}

function paperTag(value, dimension = "") {
  if (!value) return null;
  const className = dimension
    ? `paper-tag paper-tag-${dimension} paper-tag-filter`
    : "paper-tag";
  const tag = dimension
    ? createElement("button", className)
    : createElement("span", className);
  if (dimension) {
    tag.type = "button";
    tag.dataset.catalogView = dimension;
    tag.dataset.catalogFilter = value;
    tag.setAttribute("aria-label", `Filter catalog by ${value}`);
    tag.addEventListener("click", () => filterCatalogFromTag(dimension, value));
  }
  const iconName = PAPER_TAG_ICONS[dimension];
  if (iconName) tag.append(createIcon(iconName));
  tag.append(createElement("span", "paper-tag-label", value));
  return tag;
}

function externalLink(label, href, iconName = "") {
  const link = createElement("a");
  link.href = href;
  link.target = "_blank";
  link.rel = "noreferrer";
  if (iconName) {
    link.append(createIcon(iconName), createElement("span", "", label));
  } else {
    link.textContent = label;
  }
  return link;
}

function renderPaper(paper) {
  const item = createElement("li", "paper-item");
  item.style.setProperty("--paper-color", familyColor(paper));

  const body = createElement("div", "paper-body");
  const kicker = createElement("div", "paper-kicker");
  kicker.append(createElement("span", "", titleCase(paper.entry_kind)));
  if (paper.name && !["n/a", "na", "none"].includes(paper.name.toLowerCase())) {
    kicker.append(createElement("span", "system-name", paper.name));
  }
  body.append(kicker);

  const title = createElement("h3", "paper-title");
  title.append(externalLink(paper.title, paper.link));
  body.append(title);
  body.append(createElement("p", "paper-authors", paper.authors));

  const tags = createElement("div", "paper-tags");
  const tagDefinitions =
    state.view === "artifact"
      ? [
          { value: paper.artifact_family, dimension: "artifact" },
          { value: paper.artifact_type },
          { value: paper.application_domain, dimension: "application" },
        ]
      : [
          { value: paper.application_domain, dimension: "application" },
          { value: paper.artifact_family, dimension: "artifact" },
          { value: paper.artifact_type },
        ];
  tagDefinitions.forEach(({ value, dimension = "" }) => {
    const tag = paperTag(value, dimension);
    if (tag) tags.append(tag);
  });
  if (!tags.children.length) tags.append(paperTag("Unclassified"));
  body.append(tags);

  const meta = createElement("div", "paper-meta");
  meta.append(createElement("span", "paper-venue", paper.venue_display_name));
  meta.append(createElement("span", "paper-year", paper.year));
  meta.append(createElement("span", `status-pill ${paper.type}`, titleCase(paper.type)));
  const links = createElement("div", "paper-links");
  links.append(externalLink("Paper", paper.link, "ph-file-text"));
  if (paper.code) links.append(externalLink("Code", paper.code, "ph-code"));
  meta.append(links);

  item.append(body, meta);
  return item;
}

function activeFilterDefinitions() {
  const primaryLabel =
    state.primary === "__none__"
      ? state.view === "artifact"
        ? "No artifact label"
        : "No application label"
      : state.primary;
  return [
    { key: "search", label: state.search ? `Search: ${state.search}` : "" },
    { key: "primary", label: primaryLabel },
    { key: "year", label: state.year },
    { key: "kind", label: state.kind ? titleCase(state.kind) : "" },
    { key: "status", label: state.status ? titleCase(state.status) : "" },
  ].filter((filter) => filter.label);
}

function renderActiveFilters() {
  const fragment = document.createDocumentFragment();
  activeFilterDefinitions().forEach((filter) => {
    const button = createElement("button", "filter-chip");
    button.type = "button";
    button.setAttribute("aria-label", `Remove filter ${filter.label}`);
    button.append(createElement("span", "", filter.label));
    button.append(createElement("span", "", "×"));
    button.addEventListener("click", () => {
      state[filter.key] = "";
      syncControls();
      updateCatalog();
    });
    fragment.append(button);
  });
  elements.activeFilters.replaceChildren(fragment);
}

function syncControls() {
  elements.search.value = state.search;
  elements.primary.value = state.primary;
  elements.year.value = state.year;
  elements.kind.value = state.kind;
  elements.status.value = state.status;
  elements.sort.value = state.sort;
  elements.pageSize.value = String(state.pageSize);
  [
    elements.primary,
    elements.year,
    elements.kind,
    elements.status,
    elements.pageSize,
    elements.sort,
  ].forEach(refreshCustomSelect);
}

function updateUrl() {
  const params = new URLSearchParams();
  if (state.view !== "artifact") params.set("view", state.view);
  if (state.primary) params.set("filter", state.primary);
  if (state.year) params.set("year", state.year);
  if (state.kind) params.set("kind", state.kind);
  if (state.status) params.set("status", state.status);
  if (state.search) params.set("q", state.search);
  if (state.sort !== "recent") params.set("sort", state.sort);
  if (state.page > 1) params.set("page", String(state.page));
  if (state.pageSize !== DEFAULT_PAGE_SIZE) {
    params.set("perPage", String(state.pageSize));
  }
  const query = params.toString();
  history.replaceState(null, "", `${location.pathname}${query ? `?${query}` : ""}${location.hash}`);
}

function paginationItems(currentPage, totalPages) {
  if (totalPages <= 7) {
    return Array.from({ length: totalPages }, (_, index) => index + 1);
  }
  if (currentPage <= 4) return [1, 2, 3, 4, 5, "ellipsis", totalPages];
  if (currentPage >= totalPages - 3) {
    return [
      1,
      "ellipsis",
      totalPages - 4,
      totalPages - 3,
      totalPages - 2,
      totalPages - 1,
      totalPages,
    ];
  }
  return [
    1,
    "ellipsis-start",
    currentPage - 1,
    currentPage,
    currentPage + 1,
    "ellipsis-end",
    totalPages,
  ];
}

function scrollToCatalogResults() {
  const behavior = window.matchMedia("(prefers-reduced-motion: reduce)").matches
    ? "auto"
    : "smooth";
  elements.resultsPanel.scrollIntoView({ behavior, block: "start" });
}

function setCatalogPage(page) {
  state.page = page;
  updateCatalog({ resetPage: false });
  window.requestAnimationFrame(() => {
    elements.pagination
      .querySelector(`[data-page="${state.page}"]`)
      ?.focus({ preventScroll: true });
    scrollToCatalogResults();
  });
}

function renderPagination(totalPapers, firstVisible, lastVisible, totalPages) {
  elements.pagination.hidden = totalPages <= 1 || totalPapers === 0;
  if (elements.pagination.hidden) {
    elements.pagination.replaceChildren();
    return;
  }

  const summary = createElement(
    "p",
    "pagination-summary",
    `${formatNumber(firstVisible)}–${formatNumber(lastVisible)} of ${formatNumber(totalPapers)}`,
  );
  const controls = createElement("div", "pagination-controls");
  const previous = createElement("button", "pagination-direction");
  previous.type = "button";
  previous.append(createIcon("ph-arrow-left"), createElement("span", "", "Previous"));
  previous.disabled = state.page === 1;
  previous.addEventListener("click", () => setCatalogPage(state.page - 1));
  controls.append(previous);

  const pages = createElement("div", "pagination-pages");
  paginationItems(state.page, totalPages).forEach((item) => {
    if (typeof item !== "number") {
      const ellipsis = createElement("span", "pagination-ellipsis", "…");
      ellipsis.setAttribute("aria-hidden", "true");
      pages.append(ellipsis);
      return;
    }
    const page = createElement("button", "pagination-page", String(item));
    page.type = "button";
    page.dataset.page = String(item);
    page.setAttribute("aria-label", `Go to page ${item}`);
    if (item === state.page) {
      page.classList.add("is-current");
      page.setAttribute("aria-current", "page");
      page.setAttribute("aria-label", `Page ${item}, current page`);
    }
    page.addEventListener("click", () => setCatalogPage(item));
    pages.append(page);
  });
  controls.append(pages);

  const next = createElement("button", "pagination-direction");
  next.type = "button";
  next.append(createElement("span", "", "Next"), createIcon("ph-arrow-right"));
  next.disabled = state.page === totalPages;
  next.addEventListener("click", () => setCatalogPage(state.page + 1));
  controls.append(next);
  elements.pagination.replaceChildren(summary, controls);
}

function updateCatalog({ resetPage = true } = {}) {
  if (resetPage) state.page = 1;
  const papers = filteredPapers();
  const totalPages = Math.max(1, Math.ceil(papers.length / state.pageSize));
  state.page = Math.min(Math.max(1, state.page), totalPages);
  const start = (state.page - 1) * state.pageSize;
  const end = Math.min(start + state.pageSize, papers.length);
  const visible = papers.slice(start, end);
  const fragment = document.createDocumentFragment();
  visible.forEach((paper) => fragment.append(renderPaper(paper)));
  elements.paperList.replaceChildren(fragment);
  elements.resultCount.textContent = formatNumber(papers.length);
  elements.emptyState.hidden = papers.length > 0;
  renderPagination(papers.length, start + 1, end, totalPages);
  renderActiveFilters();
  updateUrl();
  elements.resultsPanel.setAttribute("aria-busy", "false");
}

function setCatalogView(view, primary = "") {
  state.view = view === "application" ? "application" : "artifact";
  state.primary = primary;
  renderFilterOptions();
  syncControls();
  updateCatalog();
}

function openCatalog(view, primary) {
  setCatalogView(view, primary);
  document.querySelector("#catalog").scrollIntoView({ behavior: "smooth" });
}

function filterCatalogFromTag(dimension, value) {
  setCatalogView(dimension, value);
  window.requestAnimationFrame(scrollToCatalogResults);
}

function clearFilters() {
  state.primary = "";
  state.year = "";
  state.kind = "";
  state.status = "";
  state.search = "";
  syncControls();
  updateCatalog();
}

function readUrlState() {
  const params = new URLSearchParams(location.search);
  state.view = params.get("view") === "application" ? "application" : "artifact";
  state.primary = params.get("filter") || "";
  state.year = params.get("year") || "";
  state.kind = params.get("kind") || "";
  state.status = params.get("status") || "";
  state.search = params.get("q") || "";
  state.sort = params.get("sort") === "title" ? "title" : "recent";
  const requestedPage = Number.parseInt(params.get("page") || "1", 10);
  const requestedPageSize = Number.parseInt(
    params.get("perPage") || String(DEFAULT_PAGE_SIZE),
    10,
  );
  state.page = Number.isFinite(requestedPage) && requestedPage > 0 ? requestedPage : 1;
  state.pageSize = PAGE_SIZE_OPTIONS.includes(requestedPageSize)
    ? requestedPageSize
    : DEFAULT_PAGE_SIZE;
}

function setupAxisTabs() {
  const tabs = [...document.querySelectorAll("[data-axis-tab]")];
  tabs.forEach((tab, index) => {
    tab.addEventListener("click", () => activateAxisTab(tab.dataset.axisTab));
    tab.addEventListener("keydown", (event) => {
      if (!["ArrowLeft", "ArrowRight"].includes(event.key)) return;
      event.preventDefault();
      const direction = event.key === "ArrowRight" ? 1 : -1;
      const next = tabs[(index + direction + tabs.length) % tabs.length];
      activateAxisTab(next.dataset.axisTab);
      next.focus();
    });
  });
}

function setupSectionNavigation() {
  const links = [
    ...document.querySelectorAll(
      '.desktop-nav a[href^="#"], .mobile-menu a[href^="#"]',
    ),
  ];
  const sections = [...new Set(links.map((link) => link.hash.slice(1)))]
    .map((id) => document.getElementById(id))
    .filter(Boolean);
  let frameRequested = false;

  function updateCurrentSection() {
    frameRequested = false;
    const activationLine = Math.min(window.innerHeight * 0.28, 220);
    let currentId = "";
    sections.forEach((section) => {
      if (section.getBoundingClientRect().top <= activationLine) {
        currentId = section.id;
      }
    });

    links.forEach((link) => {
      const isCurrent = Boolean(currentId) && link.hash === `#${currentId}`;
      link.classList.toggle("is-current", isCurrent);
      if (isCurrent) {
        link.setAttribute("aria-current", "location");
      } else {
        link.removeAttribute("aria-current");
      }
    });
  }

  function scheduleUpdate() {
    if (frameRequested) return;
    frameRequested = true;
    window.requestAnimationFrame(updateCurrentSection);
  }

  window.addEventListener("scroll", scheduleUpdate, { passive: true });
  window.addEventListener("resize", scheduleUpdate);
  updateCurrentSection();
}

function setupFilterDisclosure() {
  if (!elements.filterPanel || !elements.filterPanelToggle) return;
  const mobileFilters = window.matchMedia("(max-width: 640px)");
  const label = elements.filterPanelToggle.querySelector("span");

  function setExpanded(expanded) {
    elements.filterPanel.classList.toggle("is-expanded", expanded);
    elements.filterPanelToggle.setAttribute("aria-expanded", String(expanded));
    label.textContent = expanded ? "Hide filters" : "Show filters";
  }

  function syncForViewport() {
    setExpanded(!mobileFilters.matches);
  }

  elements.filterPanelToggle.addEventListener("click", () => {
    const expanded = elements.filterPanelToggle.getAttribute("aria-expanded") === "true";
    setExpanded(!expanded);
  });
  mobileFilters.addEventListener("change", syncForViewport);
  syncForViewport();
}

function setupCitationCopy() {
  const button = document.querySelector("[data-copy-citation]");
  const citation = document.querySelector("#survey-citation");
  const status = document.querySelector("#citation-copy-status");
  if (!button || !citation || !status) return;

  const label = button.querySelector("[data-copy-label]");
  let resetTimer = null;

  function copyWithSelection() {
    const selection = window.getSelection();
    const range = document.createRange();
    range.selectNodeContents(citation);
    selection.removeAllRanges();
    selection.addRange(range);
    const copied = document.execCommand("copy");
    if (!copied) throw new Error("Copy command was unavailable");
    selection.removeAllRanges();
  }

  async function copyCitation() {
    const citationText = citation.textContent.trim();
    try {
      if (navigator.clipboard?.writeText) {
        try {
          await navigator.clipboard.writeText(citationText);
        } catch (clipboardError) {
          copyWithSelection();
        }
      } else {
        copyWithSelection();
      }

      window.clearTimeout(resetTimer);
      button.classList.add("is-copied");
      label.textContent = "Copied";
      status.textContent = "BibTeX citation copied to clipboard.";
      resetTimer = window.setTimeout(() => {
        button.classList.remove("is-copied");
        label.textContent = "Copy BibTeX";
      }, 1800);
    } catch (error) {
      console.warn("Citation copy failed", error);
      status.textContent = "Copy failed. Select the citation text and copy it manually.";
      label.textContent = "Select manually";
    }
  }

  button.addEventListener("click", copyCitation);
}

function activateAxisTab(axis) {
  document.querySelectorAll("[data-axis-tab]").forEach((tab) => {
    const selected = tab.dataset.axisTab === axis;
    tab.setAttribute("aria-selected", String(selected));
    tab.tabIndex = selected ? 0 : -1;
  });
  const artifactPanel = document.querySelector("#artifact-panel");
  const applicationPanel = document.querySelector("#application-panel");
  const activePanel = axis === "application" ? applicationPanel : artifactPanel;
  artifactPanel.hidden = axis !== "artifact";
  applicationPanel.hidden = axis !== "application";
  activePanel.classList.remove("is-entering");
  window.requestAnimationFrame(() => activePanel.classList.add("is-entering"));
  document.dispatchEvent(new CustomEvent("aac:axischange", { detail: { axis } }));
}

function setupMiniatureCardTilt() {
  if (
    !window.matchMedia("(pointer: fine)").matches ||
    window.matchMedia("(prefers-reduced-motion: reduce)").matches
  ) {
    return;
  }

  document.querySelectorAll(".taxonomy-item, .application-item").forEach((card) => {
    card.addEventListener("pointermove", (event) => {
      const bounds = card.getBoundingClientRect();
      const horizontal = (event.clientX - bounds.left) / bounds.width - 0.5;
      const vertical = (event.clientY - bounds.top) / bounds.height - 0.5;
      card.style.setProperty("--card-tilt-x", `${(-vertical * 2.8).toFixed(2)}deg`);
      card.style.setProperty("--card-tilt-y", `${(horizontal * 3.6).toFixed(2)}deg`);
    });
    card.addEventListener("pointerleave", () => {
      card.style.removeProperty("--card-tilt-x");
      card.style.removeProperty("--card-tilt-y");
    });
  });
}

function setupMiniatureShowcaseMotion() {
  const scope = document.querySelector("#scope");
  const switcher = scope?.querySelector(".axis-switcher");
  if (!scope || !switcher) return;

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  if (!("IntersectionObserver" in window)) return;

  let activeIndex = 0;
  let timer = null;
  let scopeVisible = false;
  let interactionPaused = false;

  function visibleCards() {
    const activePanel = switcher.querySelector(".taxonomy-panel:not([hidden])");
    return [...(activePanel?.querySelectorAll(".taxonomy-item, .application-item") || [])];
  }

  function clearActive() {
    switcher
      .querySelectorAll(".taxonomy-item, .application-item")
      .forEach((card) => card.classList.remove("is-showcase-active"));
  }

  function activateCurrent() {
    const cards = visibleCards();
    if (!cards.length) return;
    activeIndex %= cards.length;
    cards.forEach((card, index) => {
      card.classList.toggle("is-showcase-active", index === activeIndex);
    });
  }

  function stop() {
    window.clearInterval(timer);
    timer = null;
  }

  function start({ immediate = true } = {}) {
    stop();
    if (reduceMotion.matches || !scopeVisible || interactionPaused || document.hidden) {
      clearActive();
      return;
    }
    if (immediate) activateCurrent();
    timer = window.setInterval(() => {
      const cards = visibleCards();
      if (!cards.length) return;
      activeIndex = (activeIndex + 1) % cards.length;
      activateCurrent();
    }, MINIATURE_SHOWCASE_INTERVAL);
  }

  function pauseForInteraction() {
    interactionPaused = true;
    stop();
    clearActive();
  }

  function resumeAfterInteraction() {
    interactionPaused = false;
    activeIndex = (activeIndex + 1) % Math.max(visibleCards().length, 1);
    start();
  }

  switcher.addEventListener("pointerenter", pauseForInteraction);
  switcher.addEventListener("pointerleave", resumeAfterInteraction);
  switcher.addEventListener("focusin", pauseForInteraction);
  switcher.addEventListener("focusout", (event) => {
    if (!switcher.contains(event.relatedTarget)) resumeAfterInteraction();
  });
  document.addEventListener("visibilitychange", () => {
    if (document.hidden) {
      stop();
      clearActive();
    } else {
      start();
    }
  });
  document.addEventListener("aac:axischange", () => {
    activeIndex = 0;
    start();
  });
  reduceMotion.addEventListener("change", () => {
    if (reduceMotion.matches) {
      stop();
      clearActive();
    } else {
      start();
    }
  });

  const observer = new IntersectionObserver(
    ([entry]) => {
      scopeVisible = entry.isIntersecting;
      if (scopeVisible) {
        start();
      } else {
        stop();
        clearActive();
      }
    },
    { threshold: 0.22 },
  );
  observer.observe(scope);
}

function setupEvents() {
  elements.search.addEventListener("input", (event) => {
    state.search = event.target.value;
    updateCatalog();
  });
  elements.primary.addEventListener("change", (event) => {
    state.primary = event.target.value;
    updateCatalog();
  });
  elements.year.addEventListener("change", (event) => {
    state.year = event.target.value;
    updateCatalog();
  });
  elements.kind.addEventListener("change", (event) => {
    state.kind = event.target.value;
    updateCatalog();
  });
  elements.status.addEventListener("change", (event) => {
    state.status = event.target.value;
    updateCatalog();
  });
  elements.sort.addEventListener("change", (event) => {
    state.sort = event.target.value;
    updateCatalog();
  });
  elements.pageSize.addEventListener("change", (event) => {
    state.pageSize = Number.parseInt(event.target.value, 10);
    updateCatalog();
  });
  document.querySelectorAll('input[name="catalog-view"]').forEach((input) => {
    input.addEventListener("change", (event) => setCatalogView(event.target.value));
  });
  elements.clearFilters.addEventListener("click", clearFilters);
  document.querySelectorAll("[data-clear-filters]").forEach((button) => {
    button.addEventListener("click", clearFilters);
  });
  window.addEventListener("popstate", () => {
    readUrlState();
    renderFilterOptions();
    syncControls();
    updateCatalog({ resetPage: false });
  });
  document.querySelectorAll(".mobile-menu a").forEach((link) => {
    link.addEventListener("click", () => link.closest("details").removeAttribute("open"));
  });
}

function setupRevealMotion() {
  const revealElements = document.querySelectorAll(".reveal");
  if (
    window.matchMedia("(prefers-reduced-motion: reduce)").matches ||
    !("IntersectionObserver" in window)
  ) {
    revealElements.forEach((element) => element.classList.add("is-visible"));
    return;
  }
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    },
    { threshold: 0.08, rootMargin: "0px 0px -40px" },
  );
  revealElements.forEach((element) => observer.observe(element));
}

function settleStalledCharts(message) {
  document.querySelectorAll(".chart-loading").forEach((loading) => {
    const error = document.createElement("p");
    error.className = "chart-error";
    error.textContent = message;
    loading.replaceWith(error);
  });
}

async function initialize() {
  setupRevealMotion();
  setupAxisTabs();
  setupSectionNavigation();
  setupFilterDisclosure();
  setupCitationCopy();
  window.setTimeout(
    () => settleStalledCharts("Chart loading timed out. Reload the page to try again."),
    10000,
  );
  try {
    const catalogUrl = document.body.dataset.catalogUrl || "data/catalog.json";
    const response = await fetch(catalogUrl);
    if (!response.ok) throw new Error(`Catalog request failed: ${response.status}`);
    state.catalog = await response.json();
    readUrlState();
    hydrateSummary();
    renderTaxonomyOverview();
    setupMiniatureShowcaseMotion();
    setupMiniatureCardTilt();
    renderFilterOptions();
    renderYearOptions();
    setupCustomSelects();
    syncControls();
    setupEvents();
    updateCatalog({ resetPage: false });
  } catch (error) {
    console.error(error);
    settleStalledCharts(
      window.location.protocol === "file:"
        ? "Charts require the published site or a local web server."
        : "The chart data could not be loaded. Reload the page to try again.",
    );
    elements.resultsPanel.setAttribute("aria-busy", "false");
    elements.paperList.replaceChildren();
    elements.emptyState.hidden = false;
    elements.emptyState.querySelector("p").textContent =
      "The catalog could not be loaded. Please try again or use the repository README.";
  }
}

initialize();
