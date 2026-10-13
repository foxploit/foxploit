<h1 align="center">🦊 foxploit</h1>

<p align="center">
  <img src="./banner.png" alt="foxploit banner" width="100%">
</p>

<p align="center">
  <a href="./contrib-heatmap.svg">
    <img src="./contrib-heatmap.svg" alt="Contribution heatmap — auto-refreshed daily" width="100%">
  </a>
</p>

<p align="center"><sub>Se regenera automáticamente cada día a las 03:00 UTC.</sub></p>

<p align="center">
  <img src="https://img.shields.io/badge/eJPT-exam%20planned%20early%202027-6d28d9?style=flat-square" alt="eJPT exam planned for early 2027">
  <img src="https://img.shields.io/badge/HackTheBox-Skilled-4c1d95?style=flat-square" alt="HackTheBox rank: Skilled">
</p>

> **Perfil en remodelación** 🚧 — Este espacio está siendo reconstruido desde cero. Los proyectos de abajo existen y funcionan, pero están pendientes de documentación completa (README, arquitectura, demos). Vuelve pronto.

<p align="center">
  <a href="#-sobre-mí">Sobre mí</a> ·
  <a href="#-proyectos-pendientes-de-remodelación-completa">Proyectos</a> ·
  <a href="#-próximamente">Próximamente</a> ·
  <a href="#-contacto">Contacto</a>
</p>

---

## 👋 Sobre mí

Estudiante de 2.º de Ciberseguridad y Data Intelligence (MSMK University) con base en **pentesting web y seguridad ofensiva**, con el objetivo de especializarme en red team y crecer hacia purple team. Preparando la certificación **eJPT**, examen previsto a principios de 2027.

Practico en Hack The Box (rango **Skilled**, 22 máquinas resueltas: 13 fáciles, 8 medias y 1 difícil) y desarrollo mis propias herramientas en Python y Bash en lugar de depender solo de las existentes.

---

## 🔧 Proyectos (pendientes de remodelación completa)

Estos repos ya tienen código funcional. Cada uno va a recibir su propio `README.md` con explicación de arquitectura, instalación y demo — de momento, aquí va el resumen:

### 🧩 [Natas Auto-Solver](https://github.com/foxploit/overthewire-solver)
Herramienta en Python y Bash que resuelve de forma automática todos los niveles del wargame **Natas** (OverTheWire): manipulación de cookies, bypass de acceso, encoding, path traversal y fuzzing.
*Pendiente: añadir los niveles de Bandit y un menú interactivo.*

### 🧨 SSTI Detection Tool
Herramienta en Python que detecta **Server-Side Template Injection** con payloads multi-motor. Versión original validada en un CTF de Hack The Box; la estoy reescribiendo desde cero.
*Pendiente: README con motores soportados y ejemplos de uso.*

### 🔀 Pull request a Tailscale ([tailscale-android #892](https://github.com/tailscale/tailscale-android/pull/892)) — Abierto
Detecté que el DNS quedaba mal configurado al desconectar y reconectar el Wi-Fi muy rápido, y propuse un arreglo para reconfigurarlo solo cuando hay una configuración nueva pendiente.

### 🏠 Homelab
Servidor Proxmox con unas 10 máquinas virtuales, monitorización con Beszel y actualizaciones automatizadas mediante scripts. Incluye Home Assistant y un gestor de inventario.

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
