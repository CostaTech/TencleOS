# Roadmap & Known Issues

This file tracks known bugs, planned fixes, and future features for both TencleOS and PancleOS.
It will be updated as issues are resolved and new goals are set.

---

## Known Bugs

### TencleOS

| ID | Status | Description |
|----|--------|-------------|
| B1 | 🔴 Open | **calc.tlang math broken** — expressions like `a + b * c` are evaluated left-to-right with no operator precedence. Needs a proper expression parser (shunting-yard algorithm). |
| B2 | 🔴 Open | **`browse` command hangs without NIC** — if the network card is not initialized or DHCP fails, `browse <ip> <port>` enters an infinite loop with no error message. |
| B3 | 🔴 Open | **`mood Desktop` calls old ASM desktop** — the command still dispatches to the old Assembly desktop instead of the newer C desktop with improved cursor and icons. |
| B4 | 🔴 Open | **TencleLang `input()` desyncs after script run** — after executing a `.tlang` script that uses `input()` or `readkey()`, the shell loses keyboard focus and may show ghost characters or duplicate prompts. |
| B5 | 🔴 Open | **TencleLang `<<While>>` loop never exits** — the loop condition is not re-evaluated correctly after each iteration. If the condition becomes false mid-run, the loop continues indefinitely. |
| B6 | ⚠️ Workaround | **Mouse broken on Oracle VirtualBox** — the PS/2 mouse driver causes keyboard lockups and corrupted input when used inside VirtualBox. Works correctly on QEMU. Workaround: disable PS/2 Mouse in VirtualBox settings, or use QEMU. |

### PancleOS

| ID | Status | Description |
|----|--------|-------------|
| P1 | 🔴 Open | **RTC not implemented** — `date` and `time` commands always return `2026-01-01 00:00:00`. Real-time clock reads are not yet wired to the CMOS chip. |
| P2 | 🔴 Open | **No scroll in VGA** — when output exceeds 25 lines, the screen wraps back to row 0 instead of scrolling up. Long `help` output gets partially overwritten. |

---

## Planned Features

### TencleOS

| Priority | Feature | Notes |
|----------|---------|-------|
| High | Fix TencleLang expression parser | Implement shunting-yard for correct operator precedence |
| High | Fix `mood Desktop` dispatch | Route to C desktop instead of old ASM desktop |
| High | Fix `<<While>>` loop condition | Re-evaluate condition at each iteration |
| Medium | IRQ12 mouse handler | Replace polling approach with interrupt-driven mouse input — may fix VirtualBox compatibility |
| Medium | Fix `input()` sync after script | Save/restore keyboard buffer state around TencleLang script execution |
| Medium | NIC guard in `browse` | Check `HAS_NIC` flag before entering network commands, print clear error if unavailable |
| Low | VirtualBox auto-detection | Detect VirtualBox at boot via CPUID or DMI strings and disable PS/2 mouse automatically |
| Low | More built-in apps | Extend the app library written in TencleLang v2 |

### PancleOS

| Priority | Feature | Notes |
|----------|---------|-------|
| High | VGA scrolling | Implement proper scroll-up when output reaches the bottom of the screen |
| High | RTC support | Read real date/time from CMOS chip |
| Medium | Persistent filesystem | Move VFS from RAM to a disk image so files survive reboots |
| Medium | More shell commands | `find`, `grep`, `cat` with line numbers, `echo` redirection |
| Low | Color theme customization | Allow changing shell colors via a config file in TencleLang |
| Low | Second distro | Explore a second distribution of TencleOS with a different purpose or audience |

---

## Completed

| Date | Item |
|------|------|
| 2026-04 | PancleOS born as first official TencleOS distribution |
| 2026-04 | VFS fully wired in PancleOS shell (ls, pwd, mkdir, rm, cp, mv) |
| 2026-04 | TencleLang interpreter warnings fixed in PancleOS |
| 2026-04 | VirtualBox mouse drain timeout added (partial workaround) |
| 2026-04 | Boot banner and `about` command added to PancleOS |
| 2026-04 | Error messages localized and improved in PancleOS shell |

---

*© 2026 CostaTech*
