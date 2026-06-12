// FNAF 4 Web Game Logic

// Audio Controller using Web Audio API
class FNAFAudio {
    constructor() {
        this.ctx = null;
        this.ambientDrone = null;
        this.ambientNoise = null;
        this.ambientGain = null;
        this.breathingTimer = null;
        this.breathingActive = false;
        this.noiseBuffer = null;
    }

    init() {
        if (this.ctx) return;
        
        // Initialize AudioContext
        const AudioContextClass = window.AudioContext || window.webkitAudioContext;
        this.ctx = new AudioContextClass();
        
        // Generate white noise buffer for ambient rumbling and breathing
        const bufferSize = this.ctx.sampleRate * 2;
        this.noiseBuffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
        const output = this.noiseBuffer.getChannelData(0);
        for (let i = 0; i < bufferSize; i++) {
            output[i] = Math.random() * 2 - 1;
        }

        this.startAmbient();
    }

    startAmbient() {
        if (!this.ctx) return;
        
        // 1. Low frequency oscillator drone (hum)
        this.ambientDrone = this.ctx.createOscillator();
        this.ambientDrone.type = 'sine';
        this.ambientDrone.frequency.setValueAtTime(55, this.ctx.currentTime); // Low hum (A1 note)
        
        const droneFilter = this.ctx.createBiquadFilter();
        droneFilter.type = 'lowpass';
        droneFilter.frequency.setValueAtTime(100, this.ctx.currentTime);
        
        this.ambientGain = this.ctx.createGain();
        this.ambientGain.gain.setValueAtTime(0.12, this.ctx.currentTime);
        
        this.ambientDrone.connect(droneFilter);
        droneFilter.connect(this.ambientGain);
        this.ambientGain.connect(this.ctx.destination);
        this.ambientDrone.start();

        // 2. Continuous wind rumble (filtered white noise)
        this.ambientNoise = this.ctx.createBufferSource();
        this.ambientNoise.buffer = this.noiseBuffer;
        this.ambientNoise.loop = true;
        
        const noiseFilter = this.ctx.createBiquadFilter();
        noiseFilter.type = 'bandpass';
        noiseFilter.frequency.setValueAtTime(90, this.ctx.currentTime);
        noiseFilter.Q.setValueAtTime(0.6, this.ctx.currentTime);
        
        const noiseGain = this.ctx.createGain();
        noiseGain.gain.setValueAtTime(0.05, this.ctx.currentTime);
        
        this.ambientNoise.connect(noiseFilter);
        noiseFilter.connect(noiseGain);
        noiseGain.connect(this.ctx.destination);
        this.ambientNoise.start();
    }

    stopAmbient() {
        try {
            if (this.ambientDrone) {
                this.ambientDrone.stop();
                this.ambientDrone.disconnect();
            }
            if (this.ambientNoise) {
                this.ambientNoise.stop();
                this.ambientNoise.disconnect();
            }
        } catch (e) {
            console.log("Ambient already stopped or inactive", e);
        }
        this.stopBreathing();
    }

    playFlashlightClick() {
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        
        const osc = this.ctx.createOscillator();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(1400, now);
        osc.frequency.exponentialRampToValueAtTime(120, now + 0.04);
        
        const gain = this.ctx.createGain();
        gain.gain.setValueAtTime(0.04, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.04);
        
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now);
        osc.stop(now + 0.05);
    }

    playDoorOpen() {
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        
        // Creaking hinges sound (oscillator frequency sweep)
        const osc = this.ctx.createOscillator();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(180, now);
        osc.frequency.linearRampToValueAtTime(280, now + 0.5);
        
        const filter = this.ctx.createBiquadFilter();
        filter.type = 'bandpass';
        filter.frequency.setValueAtTime(300, now);
        filter.Q.setValueAtTime(1.0, now);
        
        const gain = this.ctx.createGain();
        gain.gain.setValueAtTime(0, now);
        gain.gain.linearRampToValueAtTime(0.08, now + 0.1);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.5);
        
        osc.connect(filter);
        filter.connect(gain);
        gain.connect(this.ctx.destination);
        
        osc.start(now);
        osc.stop(now + 0.6);
    }

    playDoorClose() {
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        
        // Slam thud (low sine thump + noise splash)
        const osc = this.ctx.createOscillator();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(100, now);
        osc.frequency.exponentialRampToValueAtTime(30, now + 0.25);
        
        const thudGain = this.ctx.createGain();
        thudGain.gain.setValueAtTime(0.25, now);
        thudGain.gain.exponentialRampToValueAtTime(0.001, now + 0.25);
        
        osc.connect(thudGain);
        thudGain.connect(this.ctx.destination);
        osc.start(now);
        osc.stop(now + 0.3);

        const noise = this.ctx.createBufferSource();
        noise.buffer = this.noiseBuffer;
        
        const noiseFilter = this.ctx.createBiquadFilter();
        noiseFilter.type = 'lowpass';
        noiseFilter.frequency.setValueAtTime(150, now);
        
        const noiseGain = this.ctx.createGain();
        noiseGain.gain.setValueAtTime(0.1, now);
        noiseGain.gain.exponentialRampToValueAtTime(0.001, now + 0.15);
        
        noise.connect(noiseFilter);
        noiseFilter.connect(noiseGain);
        noiseGain.connect(this.ctx.destination);
        noise.start(now);
        noise.stop(now + 0.2);
    }

    startBreathing() {
        if (!this.ctx || this.breathingActive) return;
        this.breathingActive = true;
        this.playBreathingCycle();
    }

    stopBreathing() {
        this.breathingActive = false;
        if (this.breathingTimer) {
            clearTimeout(this.breathingTimer);
            this.breathingTimer = null;
        }
    }

    playBreathingCycle() {
        if (!this.ctx || !this.breathingActive) return;
        
        const noise = this.ctx.createBufferSource();
        noise.buffer = this.noiseBuffer;
        
        const filter = this.ctx.createBiquadFilter();
        filter.type = 'lowpass';
        
        const gain = this.ctx.createGain();
        
        noise.connect(filter);
        filter.connect(gain);
        gain.connect(this.ctx.destination);
        
        const now = this.ctx.currentTime;
        
        // Inhale (duration 1.4s)
        filter.frequency.setValueAtTime(200, now);
        filter.frequency.linearRampToValueAtTime(400, now + 1.2);
        gain.gain.setValueAtTime(0.001, now);
        gain.gain.linearRampToValueAtTime(0.04, now + 1.2);
        
        // Hold (0.2s)
        gain.gain.setValueAtTime(0.04, now + 1.4);
        
        // Exhale (duration 1.4s)
        filter.frequency.setValueAtTime(400, now + 1.4);
        filter.frequency.linearRampToValueAtTime(180, now + 2.8);
        gain.gain.setValueAtTime(0.04, now + 1.4);
        gain.gain.linearRampToValueAtTime(0.001, now + 2.8);
        
        noise.start(now);
        noise.stop(now + 2.9);
        
        this.breathingTimer = setTimeout(() => this.playBreathingCycle(), 3400);
    }

    playJumpscare() {
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        
        // Intense horror distortion curve
        const distortion = this.ctx.createWaveShaper();
        const curve = new Float32Array(44100);
        const k = 100;
        const deg = Math.PI / 180;
        for (let i = 0 ; i < 44100; ++i ) {
            const x = (i * 2) / 44100 - 1;
            curve[i] = ((3 + k) * x * 22 * deg) / (Math.PI + k * Math.abs(x));
        }
        distortion.curve = curve;
        distortion.oversample = '4x';

        // 3 oscillators for a harsh multi-layered scream
        const osc1 = this.ctx.createOscillator();
        osc1.type = 'sawtooth';
        osc1.frequency.setValueAtTime(240, now);
        osc1.frequency.linearRampToValueAtTime(90, now + 1.6);
        
        const osc2 = this.ctx.createOscillator();
        osc2.type = 'square';
        osc2.frequency.setValueAtTime(310, now);
        osc2.frequency.linearRampToValueAtTime(450, now + 1.6);
        
        const osc3 = this.ctx.createOscillator();
        osc3.type = 'sawtooth';
        osc3.frequency.setValueAtTime(130, now);
        osc3.frequency.linearRampToValueAtTime(40, now + 1.6);

        const gainNode = this.ctx.createGain();
        gainNode.gain.setValueAtTime(0.55, now);
        gainNode.gain.exponentialRampToValueAtTime(0.001, now + 1.6);

        osc1.connect(distortion);
        osc2.connect(distortion);
        osc3.connect(distortion);
        
        distortion.connect(gainNode);
        gainNode.connect(this.ctx.destination);
        
        // White noise layer for statics
        const noise = this.ctx.createBufferSource();
        noise.buffer = this.noiseBuffer;
        const noiseGain = this.ctx.createGain();
        noiseGain.gain.setValueAtTime(0.35, now);
        noiseGain.gain.exponentialRampToValueAtTime(0.001, now + 1.6);
        
        noise.connect(noiseGain);
        noiseGain.connect(gainNode);

        osc1.start(now);
        osc2.start(now);
        osc3.start(now);
        noise.start(now);
        
        osc1.stop(now + 1.7);
        osc2.stop(now + 1.7);
        osc3.stop(now + 1.7);
        noise.stop(now + 1.7);
    }

    play6amChime() {
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        
        // 1. Classic clock chimes (sine/triangle bells)
        const notes = [220, 277, 330, 440]; // A major chime
        notes.forEach((freq, index) => {
            const time = now + index * 0.9;
            const osc1 = this.ctx.createOscillator();
            osc1.type = 'sine';
            osc1.frequency.setValueAtTime(freq, time);
            
            const osc2 = this.ctx.createOscillator();
            osc2.type = 'triangle';
            osc2.frequency.setValueAtTime(freq * 2, time); // Harmonic
            
            const gain = this.ctx.createGain();
            gain.gain.setValueAtTime(0, time);
            gain.gain.linearRampToValueAtTime(0.18, time + 0.05);
            gain.gain.exponentialRampToValueAtTime(0.001, time + 1.6);
            
            osc1.connect(gain);
            osc2.connect(gain);
            gain.connect(this.ctx.destination);
            
            osc1.start(time);
            osc2.start(time);
            osc1.stop(time + 1.7);
            osc2.stop(time + 1.7);
        });

        // 2. Children cheering (high-pitched arpeggio chime sweep)
        const cheerStart = now + 3.4;
        const cheerNotes = [523.25, 587.33, 659.25, 783.99, 880.00, 1046.50, 1318.51, 1567.98]; // Arpeggio C5 to G6
        cheerNotes.forEach((freq, index) => {
            const t = cheerStart + index * 0.12;
            const osc = this.ctx.createOscillator();
            osc.type = 'sine';
            osc.frequency.setValueAtTime(freq, t);
            
            const gain = this.ctx.createGain();
            gain.gain.setValueAtTime(0, t);
            gain.gain.linearRampToValueAtTime(0.12, t + 0.02);
            gain.gain.exponentialRampToValueAtTime(0.001, t + 0.5);
            
            osc.connect(gain);
            gain.connect(this.ctx.destination);
            
            osc.start(t);
            osc.stop(t + 0.6);
        });
    }
}

// Game State Engine
const game = {
    // Current state variables
    status: 'start',
    time: 0,
    action_amount: 0,
    location: 'room',
    flashlightOn: false,
    
    // Server rolled states cached
    random_probability1: '',
    random_probability2: '',
    random_probability22: '',
    closet_state: '',

    // Sub-view item states
    door1Open: false,
    door2Open: false,
    closetOpen: false,

    // Audio helper
    audio: new FNAFAudio(),

    // Initialize application
    init() {
        this.bindEvents();
        this.updateFlashlightUI();
    },

    // Attach listeners
    bindEvents() {
        // Track mouse coordinates for flashlight mask
        window.addEventListener('mousemove', (e) => {
            const viewport = document.getElementById('scene-viewport');
            const rect = viewport.getBoundingClientRect();
            
            // Calculate relative coordinates in viewport
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            // Set CSS variables
            document.documentElement.style.setProperty('--flashlight-x', `${x}px`);
            document.documentElement.style.setProperty('--flashlight-y', `${y}px`);
        });

        // Keydown keyboard controls for playability
        window.addEventListener('keydown', (e) => {
            if (e.key.toLowerCase() === 'f') {
                this.toggleFlashlight();
                return;
            }

            if (this.status !== 'playing') return;

            const key = e.key.toLowerCase();
            
            // Go Back / Close with Escape, S, or Down Arrow
            if (key === 'escape' || key === 's' || e.key === 'ArrowDown') {
                if (this.location !== 'room') {
                    e.preventDefault();
                    if (this.location === 'door1') {
                        this.backFromDoor1();
                    } else if (this.location === 'door2') {
                        this.backFromDoor2();
                    } else if (this.location === 'closet') {
                        this.closeClosetAction(); // Closing closet costs an action
                    } else if (this.location === 'behind') {
                        this.navigateTo('room'); // Bed go back does not cost action
                    }
                } else {
                    // S or Down Arrow in room turns around to look at the Bed
                    e.preventDefault();
                    this.navigateTo('behind');
                }
            }
            
            // Go to Left Door with A or Left Arrow
            else if (this.location === 'room' && (key === 'a' || e.key === 'ArrowLeft')) {
                e.preventDefault();
                this.navigateTo('door1');
            }
            
            // Go to Right Door with D or Right Arrow
            else if (this.location === 'room' && (key === 'd' || e.key === 'ArrowRight')) {
                e.preventDefault();
                this.navigateTo('door2');
            }
            
            // Go to Closet with W or Up Arrow
            else if (this.location === 'room' && (key === 'w' || e.key === 'ArrowUp')) {
                e.preventDefault();
                this.navigateTo('closet');
            }
            
            // Action shortcut with Space key
            else if (e.key === ' ') {
                e.preventDefault();
                if (this.location === 'door1') {
                    if (!this.door1Open) {
                        this.toggleDoor1();
                    } else {
                        this.useDoor1Flashlight();
                    }
                } else if (this.location === 'door2') {
                    if (!this.door2Open) {
                        this.toggleDoor2();
                    } else {
                        this.useDoor2Flashlight();
                    }
                } else if (this.location === 'closet') {
                    this.openClosetAction();
                } else if (this.location === 'behind') {
                    this.useBedFlashlight();
                }
            }
        });
        document.getElementById('hud-flashlight').addEventListener('click', () => this.toggleFlashlight());

        // Also allow toggling flashlight with regular mouse clicks on the viewport
        document.getElementById('scene-viewport').addEventListener('click', (e) => {
            // Only toggle if we didn't click on an interactive button or hotspot
            if (e.target.tagName !== 'BUTTON' && !e.target.closest('.hotspot') && this.status === 'playing') {
                this.toggleFlashlight();
            }
        });

        // Navigation elements
        document.getElementById('btn-start').addEventListener('click', () => this.startGame());
        document.getElementById('btn-restart').addEventListener('click', () => this.startGame());
        document.getElementById('btn-win-restart').addEventListener('click', () => this.startGame());

        // Room hotspots navigation
        document.getElementById('hotspot-left-door').addEventListener('click', () => this.navigateTo('door1'));
        document.getElementById('hotspot-right-door').addEventListener('click', () => this.navigateTo('door2'));
        document.getElementById('hotspot-closet').addEventListener('click', () => this.navigateTo('closet'));
        document.getElementById('btn-turn-around').addEventListener('click', () => this.navigateTo('behind'));

        // Door 1 Actions
        document.getElementById('btn-door1-toggle').addEventListener('click', () => this.toggleDoor1());
        document.getElementById('btn-door1-flashlight').addEventListener('click', () => this.useDoor1Flashlight());
        document.getElementById('btn-door1-back').addEventListener('click', () => this.backFromDoor1());

        // Door 2 Actions
        document.getElementById('btn-door2-toggle').addEventListener('click', () => this.toggleDoor2());
        document.getElementById('btn-door2-flashlight').addEventListener('click', () => this.useDoor2Flashlight());
        document.getElementById('btn-door2-back').addEventListener('click', () => this.backFromDoor2());

        // Closet Actions
        document.getElementById('btn-closet-open').addEventListener('click', () => this.openClosetAction());
        document.getElementById('btn-closet-close').addEventListener('click', () => this.closeClosetAction());
        document.getElementById('btn-closet-back').addEventListener('click', () => this.closeClosetAction());

        // Bed Actions
        document.getElementById('btn-behind-flashlight').addEventListener('click', () => this.useBedFlashlight());
        document.getElementById('btn-behind-back').addEventListener('click', () => this.navigateTo('room'));
    },

    // Start a new game session
    startGame() {
        this.audio.init();
        
        // Reset overlays and HUD
        document.getElementById('start-screen').classList.remove('active');
        document.getElementById('death-screen').classList.remove('active');
        document.getElementById('win-screen').classList.remove('active');
        document.getElementById('win-screen').classList.remove('win-screen-cheering');
        document.body.classList.remove('jumpscare-triggered');
        document.getElementById('game-interface').classList.remove('hidden');

        // Reset variables
        this.status = 'playing';
        this.door1Open = false;
        this.door2Open = false;
        this.closetOpen = false;
        this.flashlightOn = false;
        this.updateFlashlightUI();
        
        // Reset visual elements
        document.getElementById('visual-door1').classList.remove('open');
        document.getElementById('visual-door1').classList.add('closed');
        document.getElementById('btn-door1-toggle').classList.remove('disabled');
        document.getElementById('btn-door1-toggle').textContent = "Open Door";
        document.getElementById('btn-door1-flashlight').classList.add('disabled');
        document.getElementById('btn-door1-back').textContent = "Go Back";
        
        document.getElementById('visual-door2').classList.remove('open');
        document.getElementById('visual-door2').classList.add('closed');
        document.getElementById('btn-door2-toggle').classList.remove('disabled');
        document.getElementById('btn-door2-toggle').textContent = "Open Door";
        document.getElementById('btn-door2-flashlight').classList.add('disabled');
        document.getElementById('btn-door2-back').textContent = "Go Back";

        document.getElementById('visual-closet').classList.remove('open');
        document.getElementById('visual-closet').classList.add('closed');

        this.clearLogs();
        this.navigateTo('room');

        // Fetch start game endpoint
        fetch('/api/start', { method: 'POST' })
            .then(res => res.json())
            .then(data => {
                this.updateHUD(data);
                data.messages.forEach(msg => this.log(msg, 'system'));
                this.cacheTurnData(data);
                this.evalRoomCues();
            })
            .catch(err => {
                console.error("Error starting game:", err);
                this.log("Error connecting to server. Is server.py running?", 'warning');
            });
    },

    // Navigation between perspectives
    navigateTo(loc) {
        this.location = loc;
        const viewport = document.getElementById('scene-viewport');
        viewport.className = `room-${loc}`;
        
        this.log(`Moved to: ${loc === 'room' ? 'Center Bedroom' : loc === 'behind' ? 'Bed' : loc}`, 'system');

        // Stop breathing sound whenever navigating unless we are in the right position
        this.audio.stopBreathing();

        // Evaluate location-specific audio cues
        if (loc === 'room') {
            this.evalRoomCues();
        } else if (loc === 'door1' && this.door1Open && this.random_probability2 === 'You hear breathing') {
            this.audio.startBreathing();
        } else if (loc === 'door2' && this.door2Open && this.random_probability22 === 'You hear breathing') {
            this.audio.startBreathing();
        }
    },

    // Cache the rolled probabilities of the current turn
    cacheTurnData(data) {
        this.random_probability1 = data.random_probability1;
        this.random_probability2 = data.random_probability2;
        this.random_probability22 = data.random_probability22;
        this.closet_state = data.closet_state;
    },

    // Evaluate breathing and closet states when in Center Bedroom
    evalRoomCues() {
        // Freddy bed breathing
        if (this.random_probability1 === 'You hear breathing.') {
            this.log("You hear heavy breathing coming from behind you...", 'warning');
        }

        // Foxy closet indicator & visual peeking eyes
        const closetIndicator = document.getElementById('closet-state-indicator');
        const closetHotspot = document.getElementById('hotspot-closet');
        if (this.closet_state === 'The closet door is slightly open.') {
            closetIndicator.classList.remove('hidden');
            closetHotspot.classList.add('foxy-peeking');
            this.log("The closet door is slightly open...", 'warning');
        } else {
            closetIndicator.classList.add('hidden');
            closetHotspot.classList.remove('foxy-peeking');
        }
    },

    // Send action to server
    sendAction(actionName) {
        // Disable flashlight on transition to simplify logic
        if (this.flashlightOn) {
            this.toggleFlashlight();
        }

        fetch('/api/action', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ action: actionName })
        })
        .then(res => res.json())
        .then(data => {
            // Process outcomes
            this.updateHUD(data);
            data.messages.forEach(msg => {
                let style = 'system';
                if (msg.includes('died') || msg.includes('killed') || msg.includes('stabbed')) {
                    style = 'warning';
                } else if (msg.includes('relieved') || msg.includes('gone') || msg.includes('Nothing')) {
                    style = 'success';
                }
                this.log(msg, style);
            });

            if (data.status === 'won') {
                this.triggerWin();
            } else if (data.status === 'dead') {
                this.triggerDeath(data.death_reason);
            } else {
                // Return to room and cache new turn values
                this.cacheTurnData(data);
                this.navigateTo('room');
            }
        })
        .catch(err => {
            console.error("Error executing action:", err);
            this.log("Server communication failed.", 'warning');
        });
    },

    // Left Door Actions
    toggleDoor1() {
        if (this.door1Open) return;
        this.door1Open = true;
        this.audio.playDoorOpen();

        const doorVisual = document.getElementById('visual-door1');
        doorVisual.classList.remove('closed');
        doorVisual.classList.add('open');

        // Toggle action buttons
        document.getElementById('btn-door1-toggle').classList.add('disabled');
        document.getElementById('btn-door1-flashlight').classList.remove('disabled');
        document.getElementById('btn-door1-back').textContent = "Wait in Dark";

        this.log("Opened Left Door.", 'system');
        this.log(this.random_probability2, this.random_probability2 === 'You dont hear or see anything.' ? 'system' : 'warning');

        // Trigger shadow visualization if blurry
        if (this.random_probability2 === 'You see something blurry') {
            document.getElementById('shadow-door1').style.opacity = '0.3';
        }

        // Trigger breathing audio if breathing
        if (this.random_probability2 === 'You hear breathing') {
            this.audio.startBreathing();
        }
    },

    useDoor1Flashlight() {
        if (!this.door1Open) return;
        
        // Temporarily force flashlight visible to user
        if (!this.flashlightOn) {
            this.toggleFlashlight();
        }
        
        // Hide shadow
        document.getElementById('shadow-door1').style.opacity = '0';
        
        setTimeout(() => {
            this.sendAction('gotodoor1_open_flashlight');
            this.resetDoor1Buttons();
        }, 600);
    },

    backFromDoor1() {
        if (this.door1Open) {
            // Corresponds to "Wait in Dark" (open door, no flashlight)
            this.sendAction('gotodoor1_open_noflashlight');
        } else {
            // Corresponds to not opening door
            this.sendAction('gotodoor1_close');
        }
        this.resetDoor1Buttons();
    },

    resetDoor1Buttons() {
        this.door1Open = false;
        document.getElementById('visual-door1').classList.remove('open');
        document.getElementById('visual-door1').classList.add('closed');
        document.getElementById('btn-door1-toggle').classList.remove('disabled');
        document.getElementById('btn-door1-flashlight').classList.add('disabled');
        document.getElementById('btn-door1-back').textContent = "Go Back";
        document.getElementById('shadow-door1').style.opacity = '0';
    },

    // Right Door Actions
    toggleDoor2() {
        if (this.door2Open) return;
        this.door2Open = true;
        this.audio.playDoorOpen();

        const doorVisual = document.getElementById('visual-door2');
        doorVisual.classList.remove('closed');
        doorVisual.classList.add('open');

        // Toggle action buttons
        document.getElementById('btn-door2-toggle').classList.add('disabled');
        document.getElementById('btn-door2-flashlight').classList.remove('disabled');
        document.getElementById('btn-door2-back').textContent = "Wait in Dark";

        this.log("Opened Right Door.", 'system');
        this.log(this.random_probability22, this.random_probability22 === 'You dont hear or see anything.' ? 'system' : 'warning');

        // Trigger shadow visualization if blurry
        if (this.random_probability22 === 'You see something blurry') {
            document.getElementById('shadow-door2').style.opacity = '0.3';
        }

        // Trigger breathing audio if breathing
        if (this.random_probability22 === 'You hear breathing') {
            this.audio.startBreathing();
        }
    },

    useDoor2Flashlight() {
        if (!this.door2Open) return;
        
        // Force flashlight visible to user
        if (!this.flashlightOn) {
            this.toggleFlashlight();
        }
        
        document.getElementById('shadow-door2').style.opacity = '0';
        
        setTimeout(() => {
            this.sendAction('gotodoor2_open_flashlight');
            this.resetDoor2Buttons();
        }, 600);
    },

    backFromDoor2() {
        if (this.door2Open) {
            this.sendAction('gotodoor2_open_noflashlight');
        } else {
            this.sendAction('gotodoor2_close');
        }
        this.resetDoor2Buttons();
    },

    resetDoor2Buttons() {
        this.door2Open = false;
        document.getElementById('visual-door2').classList.remove('open');
        document.getElementById('visual-door2').classList.add('closed');
        document.getElementById('btn-door2-toggle').classList.remove('disabled');
        document.getElementById('btn-door2-flashlight').classList.add('disabled');
        document.getElementById('btn-door2-back').textContent = "Go Back";
        document.getElementById('shadow-door2').style.opacity = '0';
    },

    // Closet Actions
    openClosetAction() {
        this.closetOpen = true;
        document.getElementById('visual-closet').classList.remove('closed');
        document.getElementById('visual-closet').classList.add('open');
        this.audio.playDoorOpen();

        if (this.closet_state === 'The closet door is slightly open.') {
            document.getElementById('shadow-foxy').style.opacity = '0.8';
        }

        setTimeout(() => {
            this.sendAction('gotocloset_open');
            this.resetClosetVisual();
        }, 600);
    },

    closeClosetAction() {
        this.audio.playDoorClose();
        this.sendAction('gotocloset_close');
        this.resetClosetVisual();
    },

    resetClosetVisual() {
        this.closetOpen = false;
        document.getElementById('visual-closet').classList.remove('open');
        document.getElementById('visual-closet').classList.add('closed');
        document.getElementById('shadow-foxy').style.opacity = '0';
    },

    // Bed Actions
    useBedFlashlight() {
        // Toggle flashlight visual
        if (!this.flashlightOn) {
            this.toggleFlashlight();
        }
        
        // Clear plush visual if Freddy was there
        if (this.random_probability1 === 'You hear breathing.') {
            document.getElementById('freddy-plush').style.opacity = '0';
        }

        setTimeout(() => {
            this.sendAction('lookbehind');
            // Re-enable opacity state default
            document.getElementById('freddy-plush').style.opacity = '';
        }, 800);
    },

    // Flashlight Toggle logic
    toggleFlashlight() {
        if (this.status !== 'playing') return;
        
        this.flashlightOn = !this.flashlightOn;
        this.audio.playFlashlightClick();
        this.updateFlashlightUI();
    },

    updateFlashlightUI() {
        const hudFlashlight = document.getElementById('display-flashlight');
        if (this.flashlightOn) {
            document.body.classList.remove('flashlight-off');
            document.body.classList.add('flashlight-on');
            hudFlashlight.textContent = "ON";
            hudFlashlight.className = "hud-value status-on";
        } else {
            document.body.classList.remove('flashlight-on');
            document.body.classList.add('flashlight-off');
            hudFlashlight.textContent = "OFF";
            hudFlashlight.className = "hud-value status-off";
        }
    },

    // HUD updating
    updateHUD(data) {
        this.time = data.time;
        this.action_amount = data.action_amount;
        
        document.getElementById('display-time').textContent = `${data.time === 0 ? '12' : data.time} AM`;
        document.getElementById('display-actions').textContent = `${data.action_amount}/5`;
    },

    // Console printing logs
    log(message, type = 'system') {
        const consoleLogs = document.getElementById('console-logs');
        const entry = document.createElement('div');
        entry.className = `console-entry ${type}`;
        
        // Prepend cursor mark
        entry.textContent = `> ${message}`;
        consoleLogs.appendChild(entry);
        
        // Auto scroll to bottom
        consoleLogs.scrollTop = consoleLogs.scrollHeight;
    },

    clearLogs() {
        document.getElementById('console-logs').innerHTML = '';
    },

    // Game Over Trigger
    triggerDeath(reason) {
        this.status = 'dead';
        this.audio.stopAmbient();
        
        // Trigger jumpscare visuals and screech
        document.body.classList.add('jumpscare-triggered');
        this.audio.playJumpscare();

        // Reveal death screen after jumpscare animation ends
        setTimeout(() => {
            document.getElementById('death-screen').classList.add('active');
            document.getElementById('death-reason').textContent = reason;
        }, 1500);
    },

    // Game Win Trigger
    triggerWin() {
        this.status = 'won';
        this.audio.stopAmbient();
        
        document.getElementById('win-screen').classList.add('active');
        
        // Trigger clock animation transition to 6 AM
        setTimeout(() => {
            document.getElementById('win-screen').classList.add('win-screen-cheering');
            this.audio.play6amChime();
        }, 1000);
    }
};

// Initialize game on window load
window.addEventListener('DOMContentLoaded', () => {
    game.init();
});
