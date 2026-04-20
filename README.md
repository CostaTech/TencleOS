# TencleOS
# TencleOS & PancleOS

> *Two operating systems. One story.*

---

## The Story

It all started with a simple idea — what if I built my own operating system from scratch?

I had no roadmap, no team, just curiosity and a lot of free time. That idea became **TencleOS**: a bare-metal, 32-bit OS targeting x86 hardware, built entirely from the ground up. The early days were exciting. Things were taking shape — a working bootloader, a VGA text driver, a keyboard driver, a basic shell. It felt real. It felt alive.

Along the way, I also created **TencleLang** — a custom scripting language built directly into TencleOS, originally written in the same language as the OS itself. It gave the system its own identity: you could write and run scripts from inside the shell, turning a bare kernel into something that actually felt usable. You can find the standalone project here: [github.com/CostaTech/TencleLang](https://github.com/CostaTech/TencleLang).

Then things started to fall apart.

At some point, the codebase became a mess. Features clashed with each other, the boot sequence would silently fail, and what was once a working system started refusing to load at all. Nothing booted. Nothing worked. The project I had poured hours into had turned into something I could barely recognize, let alone run. I sat on it for a while, unsure whether to fix it or abandon it entirely.

Eventually, I made the decision: **start over**.

Not a patch. Not a hotfix. A complete rewrite — but this time, with everything I had learned the hard way. I knew what mistakes to avoid, what architecture made sense, and what I actually wanted the OS to look like. The result was a new TencleOS: cleaner, faster, more cohesive, and more complete than anything the original had ever been. It had a proper shell, a desktop environment, PS/2 mouse support, basic networking, and TencleLang fully integrated.

That momentum didn't stop there.

Looking back at the ruins of the original TencleOS, I realized it wasn't entirely worthless — it was just broken. So I did what felt right: I dusted it off, stripped it down to the parts that still made sense, and rebuilt it with a different vision. This time, it wouldn't try to compete with the new TencleOS. Instead, it would stand on its shoulders.

That became **PancleOS**.

PancleOS is a distribution of TencleOS — lighter, more focused, with its own shell, its own filesystem, and its own identity. Think of it the same way you'd think of the relationship between Linux and its distributions: one core, many expressions.

```
TencleOS  ──►  PancleOS

(just like Linux ──► Kali, Arch, Android)
```

The two projects now live together in this repository. Different in character, connected by history.

