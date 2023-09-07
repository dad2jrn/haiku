async function fetchHaiku() {
    try {
        const response = await fetch('/haiku');
        const data = await response.json();
        const haikuDiv = document.getElementById('haiku');
        haikuDiv.textContent = data.haiku;

        // Display the copy-to-clipboard glyph
        const copyGlyph = document.getElementById('copyGlyph');
        copyGlyph.style.display = 'inline-block';

    } catch (error) {
        console.error('Error fetching haiku:', error);
    }
}

function copyToClipboard() {
    const haikuText = document.getElementById('haiku').textContent;

    // Create a temporary textarea to copy the content
    const textarea = document.createElement('textarea');
    textarea.value = haikuText;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);

    alert('Haiku copied to clipboard!');
}