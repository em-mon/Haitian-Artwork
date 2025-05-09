import { extractColors } from "https://cdn.skypack.dev/extract-colors";

document.querySelectorAll(".images").forEach(button => {
    button.addEventListener("click", async () => {
        const img = button.querySelector("img");
  
        if (!img.complete) {
            alert("Image not fully loaded yet!");
            return;
        }
    
        try {
            const colors = await extractColors(img);
            console.log("Extracted colors:", matchColors(colors));
        } catch (error) {
            console.error("Color extraction failed:", error);
        }
    });
});

function matchColors(colorsArr) {
    const colorsToMeaning = {};

    for (const color of colorsArr) {
        const r = color.red;
        const g = color.green;
        const b = color.blue;

        // Check if red
        if (r >= 150 && r <= 255 && g <= 100 && b <= 100) {
            colorsToMeaning["Red"] = ["Red is a powerful color representing strength, passion, and vitality."];
            continue;
        }

        // Check if blue
        if (r <= 100 && g <= 245 && b >= 150 && b <= 255) {
            colorsToMeaning["Blue"] = ["Blue symbolizes peace and the spiritual realm."];
            continue;
        }

        // Check if green
        if (r <= 150 && g >= 100 && g <= 255 && b <= 150) {
            colorsToMeaning["Green"] = ["Green represents life, growth, and nature. It symbolizes fertility and renewal and is often used in paintings depicting lush landscapes and agricultural scenes."];
            continue;
        }

        // Check if yellow
        if (r >= 200 && r <= 255 && g >= 200 && g <= 255 && b <= 100) {
            colorsToMeaning["Yellow"] = ["Yellow signifies happiness, energy, and the sun. It also symbolizes wealth and prosperity."];
            continue;
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
