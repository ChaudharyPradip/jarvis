var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition;
const mic = document.querySelector(".mic");

// Animation Configuration Variables declaration
let audioCtx;
let distortion;
let gainNode;
let biquadFilter;
let analyser;
let tracks = [];
let isListening = false;

if (!navigator.mediaDevices.getUserMedia) {
    alert("getUserMedia not supported on your browser!");
}

// Fetching data from api
async function getData(message) {
    const response = await fetch("https://marojarvis.herokuapp.com/api/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message })
    });

    data = await response.json();
    return data.data;
}

async function runSpeechRecognition() {
    if (!isListening) {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({
                audio: true
            });
            isListening = true;

            tracks = stream.getTracks();
            source = audioCtx.createMediaStreamSource(stream);
            source.connect(distortion);
            distortion.connect(biquadFilter);
            biquadFilter.connect(gainNode);
            gainNode.connect(analyser);
            analyser.connect(audioCtx.destination);

            requestAnimationFrame(function log() {
                let bufferLength = analyser.frequencyBinCount;
                let dataArray = new Uint8Array(bufferLength);
                analyser.getByteFrequencyData(dataArray);
                const level = Math.max.apply(null, dataArray);
                mic.style.setProperty("--border", `${level / 5}px`);
                requestAnimationFrame(log);
            });
        } catch (err) {
            console.log("The following gUM error occured: " + err);
        }
    }

    // get output div reference
    let output = document.querySelector(".output");
    // new speech recognition object
    let recognition = new SpeechRecognition();

    recognition.onspeechend = function () {
        isListening = false;
        recognition.stop();
        tracks.forEach((track) => {
            track.stop();
        });
    };

    recognition.onresult = function (event) {
        let transcript = event.results[0][0].transcript;
        let req = document.createElement("div");
        req.textContent = transcript;
        req.classList.add("request");
        output.appendChild(req);
        output.scrollTop = output.scrollHeight;

        addResData(transcript).then((res) => {
            output.appendChild(res);
            output.scrollTop = output.scrollHeight;
        });
    };

    // start recognition
    recognition.start();
}

async function addResData(transcript) {
    response = await getData(transcript);
    let res = document.createElement("div");
    if (response == null) {
        res.textContent = "Could not get any result";
    } else {
        res.textContent = response;
    }
    res.classList.add("response");
    readOutLoud(res.textContent);
    return res;
}

function readOutLoud(message) {
    let speech = new SpeechSynthesisUtterance();

    // Set the text and voice attributes.
    speech.text = message;
    speech.volume = 1;
    speech.rate = 1;
    speech.pitch = 1;

    window.speechSynthesis.speak(speech);
}

mic.addEventListener("click", () => {
    // Animation configuration
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    distortion = audioCtx.createWaveShaper();
    gainNode = audioCtx.createGain();
    biquadFilter = audioCtx.createBiquadFilter();
    analyser = audioCtx.createAnalyser();
    analyser.minDecibels = -90;
    analyser.maxDecibels = -10;
    analyser.fftSize = 256;
    runSpeechRecognition();
});
