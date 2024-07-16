# ScannerCrystalCalc
A calculator for old-school crystal-controlled scanners

***How it works***

In the 1970s and 1980s, many radio scanners were controlled by 2-pin oscillator modules called "crystals." Many of us amateurs still use crystals for frequency control.

Crystals are cut according to their resonant frequencies, so as the crystal gets thinner, the frequency gets higher. Unfortunately, crystals will only work up to a certain frequency range, usually 50 or 60MHz, before they begin to become too fragile to oscillate over long periods of time.

With the advent of PLL and even DDS, crystals for frequency control have gone by the wayside, meaning that crystals are only used for applications for timing, such as in computers.

***How Do We Solve This?***

So the big dilemma we have here is that crystals cut for 155MHz would break the instant voltage is applied, so we rely on what is known as overtones or harmonics. Crystals will usually oscillate on 3rd, 5th, or even 7th overtones. If you're musically inclined like me, frequencies that vibrate and resonate release what are known as overtones. These become other frequencies, usually in multiples. So, a 16MHz crystal, found mainly on Arduino boards, has resonant frequencies at 32, 48, and 64MHz. They can even go up to 144MHz - right at the start of the 2m band!

Scanners in the 70s and 80s relied upon circuitry that would filter and enhance these overtone frequencies. Let's take the frequency 156.210, a popular public safety frequency near me. To calculate the 156.210 crystal's ACTUAL frequency, we'd need to use this formula:

(156.210 - 10.7)/3

This would give us our base frequency that the crystal resonates at, which is around 48.50333MHz.

Now, here's where it gets tricky...that's the VHF-Hi band...

* For VHF-Lo (30-50MHz): (Receive Freq) + IF

* For VHF-Hi (150-174MHz): (Receive Freq - IF)/3

* For UHF (450-470MHz): (Receive Freq - IF)/9



IF is intermediate frequency. For Regency/RadioShack/generic scanners, use 10.7MHz. For Bearcat or explicitly stated scanners, use 10.8MHz.

If you have an old crystal-controlled radio lying around, why not put a DDS on it that you've tuned to using one of these equations? If my calculations are correct...you should be able to restore it using modern technology!
