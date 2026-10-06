# 🦊 foxploit

<p align="center">
  <img src="./assets/banner.png" alt="foxploit banner" width="100%">
</p>

> **Perfil en remodelación** 🚧 — Este espacio está siendo reconstruido desde cero. Los proyectos de abajo existen y funcionan, pero están pendientes de documentación completa (README, arquitectura, demos). Vuelve pronto.

---

## 👋 Sobre mí

Estudiante de Ciberseguridad (HND Pearson BTEC, MSMK University) enfocado en **red team / offensive security**. Preparando la certificación **CPTS** (HTB Academy) y empezando con la **eJPT**. Activo en CTF con el equipo **0xCORE** — Hacker rank en HackTheBox.

Me gusta construir herramientas propias en lugar de depender solo de las existentes: recon automatizado, detección de vulnerabilidades, y pequeños agentes que ayudan en el proceso ofensivo.

---

## 🔧 Proyectos (pendientes de remodelación completa)

Estos repos ya tienen código funcional. Cada uno va a recibir su propio `README.md` con explicación de arquitectura, instalación y demo — de momento, aquí va el resumen:

### 🧩 Natas Auto-Solver
Script que automatiza la resolución de los niveles del wargame **Natas** (OverTheWire), encadenando técnicas de explotación nivel a nivel.
*Pendiente: documentación de cada técnica usada por nivel.*

### 🧨 SSTI-Python
Detector y probador de payloads de **Server-Side Template Injection** en Python — identifica el motor de plantillas y lanza los payloads correspondientes.
*Pendiente: README con motores soportados y ejemplos de uso.*

### 🛡️ Phishing Report
Herramienta/proceso para el análisis y reporte de intentos de phishing.
*Pendiente: documentación del flujo de análisis.*

### ⛽ Fuel Radar
Aplicación standalone para localizar gasolineras cercanas y comparar precios.
*Pendiente: README con stack y capturas.*

---

## 🚀 Próximamente

- [ ] README completo en cada repo (objetivo, stack, instalación, demo)
- [ ] Subir **limscan** — herramienta modular de recon en bash
- [ ] Writeups de máquinas de HackTheBox (PaperWork, SmartHIRE, Helix, CCTV, Kobold)

### 🦊 Herramientas de ataque pendientes de desarrollar

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

---

## 📫 Contacto

- GitHub: [@foxploit](https://github.com/foxploit)
- HackTheBox: nivel 40, rango Hacker — equipo 0xCORE
