<h1 align="center">🦊 foxploit</h1>

<p align="center">
  <img src="./banner.png" alt="foxploit banner" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/CPTS-in%20progress-8b5cf6?style=flat-square" alt="CPTS in progress">
  <img src="https://img.shields.io/badge/eJPT-starting-6d28d9?style=flat-square" alt="eJPT starting">
  <img src="https://img.shields.io/badge/HackTheBox-Hacker-4c1d95?style=flat-square" alt="HackTheBox rank: Hacker">
  <img src="https://img.shields.io/badge/CTF%20team-0xCORE-c4b5fd?style=flat-square" alt="CTF team: 0xCORE">
</p>

> **Perfil en remodelación** 🚧 — Este espacio está siendo reconstruido desde cero. Los proyectos de abajo existen y funcionan, pero están pendientes de documentación completa (README, arquitectura, demos). Vuelve pronto.

<p align="center">
  <a href="#-sobre-mí">Sobre mí</a> ·
  <a href="#-actividad">Actividad</a> ·
  <a href="#-proyectos-pendientes-de-remodelación-completa">Proyectos</a> ·
  <a href="#-próximamente">Próximamente</a> ·
  <a href="#-contacto">Contacto</a>
</p>

---

## 👋 Sobre mí

Estudiante de Ciberseguridad (HND Pearson BTEC, MSMK University) enfocado en **red team / offensive security**. Preparando la certificación **CPTS** (HTB Academy) y empezando con la **eJPT**. Activo en CTF con el equipo **0xCORE** — rango **Hacker** en HackTheBox.

Me gusta construir herramientas propias en lugar de depender solo de las existentes: recon automatizado, detección de vulnerabilidades, y pequeños agentes que ayudan en el proceso ofensivo.

---

## 📊 Actividad

<p align="center">
  <a href="./contrib-heatmap.svg">
    <img src="./contrib-heatmap.svg" alt="Contribution heatmap — auto-refreshed daily" width="100%">
  </a>
</p>

<p align="center"><sub>Se regenera automáticamente cada día a las 03:00 UTC.</sub></p>

---

## 🔧 Proyectos (pendientes de remodelación completa)

Estos repos ya tienen código funcional. Cada uno va a recibir su propio `README.md` con explicación de arquitectura, instalación y demo — de momento, aquí va el resumen:

### 🧩 [Natas Auto-Solver](https://github.com/foxploit/overthewire-solver)
Script que automatiza la resolución de los niveles del wargame **Natas** (OverTheWire) — **34/34 niveles resueltos**, encadenando técnicas de explotación nivel a nivel.
*Pendiente: documentación de cada técnica usada por nivel.*

### 🧨 SSTI-Python
Detector y probador de payloads de **Server-Side Template Injection** en Python — identifica el motor de plantillas y lanza los payloads correspondientes.
*Pendiente: README con motores soportados y ejemplos de uso.*

### 🛡️ Phishing Report
Herramienta/proceso para el análisis y reporte de intentos de phishing.
*Pendiente: documentación del flujo de análisis.*

### ⛽ Fuel Radar
Aplicación standalone para localizar gasolineras cercanas y comparar precios en tiempo real.
*Pendiente: README con stack y capturas.*

---

## 🚀 Próximamente

- [ ] README completo en cada repo (objetivo, stack, instalación, demo)
- [ ] Subir **limscan** — herramienta modular de recon en bash
- [ ] Writeups de máquinas de HackTheBox (PaperWork, SmartHIRE, Helix, CCTV, Kobold)

<details>
<summary><strong>🦊 Herramientas de ataque pendientes de desarrollar</strong></summary>
<br>

- [ ] **Proxy MITM propio** — interceptación y manipulación de tráfico HTTP/HTTPS (al estilo Burp/mitmproxy, pero hecho desde cero)
- [ ] **Port/service scanner** — escáner de puertos y fingerprinting de servicios, más rápido/ligero que nmap para recon inicial
- [ ] **Subdomain enumerator** — enumeración de subdominios combinando fuerza bruta + fuentes pasivas (certificate transparency, APIs públicas)
- [ ] **Web vuln scanner básico** — detección automatizada de XSS, SQLi y path traversal sobre formularios/endpoints
- [ ] **Hash cracker distribuido** — wrapper sobre hashcat/john con gestión de wordlists y reglas propias
- [ ] **Wordlist generator contextual** — genera diccionarios a partir de OSINT de un objetivo (nombres, fechas, empresa)
- [ ] **C2 framework minimalista** — servidor de comando y control simple para laboratorios propios (no producción)
- [ ] **Privesc checker (Linux/Windows)** — alternativa propia a linPEAS/winPEAS con output más limpio
- [ ] **Payload generator / encoder** — generación y ofuscación de payloads para evadir detección básica en entornos de laboratorio
- [ ] **OSINT recon tool** — agregador de información pública sobre un dominio/empresa (empleados, tecnologías, leaks conocidos)
- [ ] **Reverse shell manager** — gestor de listeners/shells múltiples con interfaz centralizada

</details>

---

## 📫 Contacto

- GitHub: [@foxploit](https://github.com/foxploit)
- HackTheBox: nivel 40, rango Skilled
