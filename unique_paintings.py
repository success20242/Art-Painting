import matplotlib.pyplot as plt
import numpy as np
import datetime
import random
import os

# ===== CONFIG =====
quotes = [
    "Circle of Life","Harmony in Colors","The Dance of Energy","Adinkra Spirit",
    "Every Path Tells a Story","Whispers of the Ancestors","Flow of Creation",
    "The Hidden Pattern","Soulful Lines","The Beauty Within","Colors Speak",
    "Shapes of Thought","Infinite Paths","Cosmic Flow","Silent Harmony",
    "The Art of Balance","Echoes of Nature","Mindful Strokes","Mystic Patterns",
    "The Secret Garden","Life in Motion","Waves of Time","Celestial Vibes",
    "Radiant Energy","Threads of Destiny","Spirals of Joy","The Hidden Path",
    "Inner Universe","Dance of Shadows","Colors of Hope","Journey of Light",
    "Sacred Geometry","The Painted Soul","Vibrant Mind","The Flow Within",
    "Harmony in Chaos","Wisdom in Colors","The Brush of Life","Patterns of Fate",
    "Whispering Colors","Dreaming in Lines","The Art of Silence","Cosmic Spirals",
    "Mystical Hues","The Hidden Dance","Infinite Horizons","The Painted Story",
    "Light and Shadow","Soulful Patterns","Nature's Palette","The Geometry of Life",
    "The Inner Spiral","Abstract Dreams","Flowing Colors","The Sacred Line",
    "Echoing Shapes","Spirals of Destiny","The Painted Mind","Colors of Emotion",
    "Mystic Flow","The Brush of Time","Inner Reflections","The Vibrant Path",
    "Dance of Creation","The Painted Spirit","Lines of Infinity","The Hidden Canvas",
    "Soulful Geometry","The Whispering Brush","Colors of the Ancestors","The Silent Dance",
    "Patterns of the Heart","The Flowing Mind","Radiant Horizons","Mystic Brushwork",
    "The Sacred Spiral","Lines of Wisdom","The Painted Journey","Infinite Brushstrokes",
    "Vibrant Echoes","The Hidden Palette","Soulful Vibrance","The Dance of Shadows",
    "Colors of Dreams","Mystical Lines","The Brush of Harmony","The Painted Flow",
    "Echoes of Light","The Spiraling Mind","Flowing Harmony","The Geometry of Soul",
    "The Hidden Energy","Lines of Creation","Mystic Palette","The Painted Whisper",
    "The Cosmic Brush","Colors in Motion","The Art of Reflection","The Vibrant Canvas",
    "Patterns of the Soul","The Hidden Flow","Soulful Lines of Life","The Brush of Joy",
    "Mystic Horizons","The Painted Path","The Flowing Canvas","Lines of Inspiration",
    "The Sacred Brush","Echoing Vibrance","The Art of Being","The Infinite Spiral"
]

signature = "Onyekachi Art"
history_file = "art_history.txt"
output_dir = "artworks"  # folder for generated images
num_artworks = 7

# ===== CREATE OUTPUT FOLDER =====
os.makedirs(output_dir, exist_ok=True)

# ===== LOAD PREVIOUS SEEDS =====
if os.path.exists(history_file):
    with open(history_file, "r") as f:
        used_seeds = set(int(line.strip()) for line in f.readlines())
else:
    used_seeds = set()

# ===== GENERATE UNIQUE ARTWORKS =====
for n in range(num_artworks):
    while True:
        seed = random.randint(0, 10_000_000)
        if seed not in used_seeds:
            used_seeds.add(seed)
            break

    random.seed(seed)
    np.random.seed(seed)

    title = random.choice(quotes)

    fig, ax = plt.subplots(figsize=(6,6))
    ax.set_facecolor("white")
    ax.axis("off")

    brush_shapes = ['o','s','^']
    num_strokes = 500
    for _ in range(num_strokes):
        x, y = np.random.rand(2)
        size = np.random.rand() * 500
        color = np.random.rand(3,)
        shape = random.choice(brush_shapes)
        ax.scatter(x, y, s=size, c=[color], alpha=0.6, marker=shape)

    # Label + Signature
    plt.text(0.5, -0.08, title, ha='center', va='top',
             fontsize=16, fontweight='bold', color="black", transform=ax.transAxes)
    plt.text(0.98, 0.02, signature, ha='right', va='bottom',
             fontsize=10, color="gray", alpha=0.7, transform=ax.transAxes)

    today = datetime.date.today().strftime("%Y-%m-%d")
    filename = f"{output_dir}/artwork_{today}_{seed}.png"
    plt.savefig(filename, dpi=300, bbox_inches="tight")
    plt.close(fig)

    print(f"Artwork saved as {filename} with label: {title}")

# ===== UPDATE HISTORY =====
with open(history_file, "w") as f:  # overwrite to keep history clean
    for s in used_seeds:
        f.write(f"{s}\n")

print(f"{num_artworks} unique artworks generated successfully!")
