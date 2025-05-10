import { extractColors } from "https://cdn.skypack.dev/extract-colors";

async function analyzeImage(img) {
    const options = {
        pixels: 64000,
        distance: 0.21,
        colorValidator: (red, green, blue, alpha = 255) => alpha > 250,
        saturationDistance: 0.2,
        lightnessDistance: 0.2,
        hueDistance: 0.083333333,
    };
    
    try {
        const colors = await extractColors(img, options);
        console.log(colors);
        const result = matchColors(colors);
        const outputDiv = document.getElementById("colorResults");
        outputDiv.innerHTML = "";

        for (const [colorName, meaning] of Object.entries(result)) {
            const colorSection = document.createElement("div");
            const vodou = matchVodou(colorName);
            colorSection.innerHTML = `<strong>${colorName}</strong>: ${meaning} <strong>In Haitian Vodou</strong> ${vodou}`;
            outputDiv.appendChild(colorSection);
            outputDiv.appendChild(document.createElement("br"));
        }
    } catch (error) {
        console.error("Color extraction failed:", error);
    }
}

document.querySelectorAll(".images").forEach(button => {
    button.addEventListener("click", async () => {
        const img = button.querySelector("img");
        if (!img.complete) {
            alert("Image not fully loaded yet!");
            return;
        }

        await analyzeImage(img); 
    });
});

const fileInput = document.getElementById("imageUpload");
const preview = document.getElementById("preview");

fileInput.addEventListener("change", () => {
    const file = fileInput.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = () => {
        const img = new Image();
        img.src = reader.result;

        img.onload = () => {
            preview.innerHTML = ""; 
            preview.appendChild(img); 
            analyzeImage(img); 
        };
    };
    reader.readAsDataURL(file);
});

function matchColors(colorsArr) {
    const colorsToMeaning = {};

    for (const color of colorsArr) {
        const r = color.red;
        const g = color.green;
        const b = color.blue;

        // Check if red
        if (r >= 150 && r <= 255 && g <= 166 && b <= 155) {
            colorsToMeaning["Red"] = ["Red is a powerful color representing strength, passion, and vitality."];
        }

        // Check if blue
        if (r <= 100 && g <= 245 && b >= 150 && b <= 255) {
            colorsToMeaning["Blue"] = ["Blue symbolizes peace and the spiritual realm."];
        }

        // Check if green
        if (r <= 150 && g >= 80 && g <= 255 && b <= 100) {
            colorsToMeaning["Green"] = ["Green represents life, growth, and nature. It symbolizes fertility and renewal and is often used in paintings depicting lush landscapes and agricultural scenes."];
        }

        // Check if yellow
        if (r >= 190 && r <= 255 && g >= 218 && g <= 255 && b <= 234) {
            colorsToMeaning["Yellow"] = ["Yellow signifies happiness, energy, and the sun. It also symbolizes wealth and prosperity."];
        }

        // Check if black
        if (r <= 60 && g <= 60 && b <= 60) {
            colorsToMeaning["Black"] = ["Black is a complex color that can symbolize death, mystery, and the unknown."];
            continue;
        }

        // Check if white
        if (r >= 220 && g >= 220 && b >= 220) {
            colorsToMeaning["White"] = ["White stands for purity, light, and spirituality. It is often used in religious contexts and rituals to represent the divine and the sacred."];
            continue;
        }
    }

    return colorsToMeaning;
}

function matchVodou(color) {
    switch (color) {
        case "Red":
            return `red ribbons are commonly used in Vodou rituals, 
                    tied to trees to ward off illness or as part of offerings to specific lwa.
                    Ezili Freda, the lwa of love and war, is often depicted in red.`;
        case "Blue":
            return `blue bodies of water are where Vodou rituals can commonly occur right by. 
                    This is in honor of Agwe, the lwa of the sea, whom is associated with the color
                    blue and sea-related symbols like shells and oars.`;
        case "Green":
            return `green imagery can be used to represent Grand Bois, a nature-oriented lwa closely
                    associated with trees, plants, and herbs, which also serve as offerings in rituals.`;
        case "Yellow":
            return `yellow is used to invoke certain lwa and energies during rituals. This color also
                    symbolizes the lwa of trade and commerce, Ayizan, who is known to grant wealth and success.`;
        case "Black":
            return `black is associated with the lwa of the dead. More specifically, Baron Samedi,
                    the spirit of death and the underworld is often depicted in black, as a skeleton, or 
                    in dark, burial attire. `;
        case "White":
            return `white clothing, offerings, and decorations are often used in Vodou ceremonies to create a sense
                    of connection with the lwa. Unlike the other colors, white usually isn't
                    tied to one specific lwa.`;
    }
}