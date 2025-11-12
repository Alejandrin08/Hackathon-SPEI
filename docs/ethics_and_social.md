





<img src="/Users/elrevo/Devel/hackaton/UI/logo-banca-inclusiva.png" alt="Logo B-Accesible" style="width:170px; border-radius:12px;" />

<h1 align="center">B-Accesible</h1>

<p align="center"><em>"La banca que te acompaña. Tecnología que te entiende"</em></p>

# 🧭 Declaración Ética y de Impacto Social  

### Proyecto: **Banca Inclusiva con IA Adaptativa y Accesible**

## 🇲🇽 Contexto Mexicano

En México, **más del 50% de la población adulta no tiene acceso a servicios financieros formales**, y cerca del **40% presenta baja alfabetización digital o funcional**.  
Según datos de **INEGI (ENDUTIH 2023)**[^7] y la **Comisión Nacional Bancaria y de Valores (CNBV)**:[^3]

- Solo **4 de cada 10 personas** usan apps financieras o de banca móvil.  
- En zonas rurales y comunidades indígenas, la adopción es inferior al **20%**.  
- Existen **barreras culturales, lingüísticas, cognitivas y de accesibilidad** que excluyen a millones de personas de los servicios financieros digitales[^10].  
- Las personas con **discapacidad visual o cognitiva**, así como **adultos mayores,** enfrentan un mayor riesgo de fraude o de dependencia de terceros.
- 4.4 millones de personas que no utilizan internet simplemente porque no lo requieren o porque no se sienten seguras al utilizar esta tecnología [^2].

Este proyecto nace de la necesidad de **reducir la brecha de inclusión digital y financiera**, creando una aplicación de **banca guiada, accesible y segura que aproveche tecnologías emergentes, como la IA, para adaptar la interfaz a las capacidades y al contexto del usuario, sin comprometer su privacidad ni su autonomía.**

---

## 🌍 Propósito

B-Accesible busca **democratizar el acceso a la banca digital**, facilitando operaciones como consulta de saldo, envío y recepción de dinero y pago de servicios para:

- Personas con **baja alfabetización** o **escasa experiencia tecnológica**.  
- Personas **con discapacidad visual o motriz**.  
- Personas con necesidades de apoyo mediante **guía por voz**.  
- Adultos mayores que requieren **retroalimentación más clara y segura**.
- Personas que no requieren del manejo de **términos técnicos complejos**

El principio rector es **"inclusión con dignidad"**:  

Usar la IA no para automatizar decisiones, sino para **acompañar y empoderar** al usuario. Las personas siempre están en el centro; la tecnología solo es un aliado.

---

## 🧩 Principios Éticos Fundamentales

El desarrollo de B-Accesible se guía por los siguientes marcos:

- **Menlo Report (2012)** — Ética en investigación de sistemas de información [^11].  
- **Carta de Derechos Digitales de México (2022)**.  [^14]
- **Lineamientos de Ética en Inteligencia Artificial de la UNESCO (2021)**.[^18]
- **Ley Federal de Protección de Datos Personales en Posesión de los Particulares (LFPDPPP)**.  
- **Estrategia Nacional de Ciberseguridad de México (2017) e iniciativa de ley federal de ciberseguridad y confianza digital (2024)** [^4].
- **Iniciativa de ley general de neuroderechos y neurotecnologías (2024)** [^5].
- **Propuesta de Marco Normativo para la Inteligencia Artificial (IA) en México (2025)** [^15].



### Principios Clave y su Aplicación

| Principio                                                    | Descripción                                                  | Característica de B-Accesible                                |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Autonomía y consentimiento informado**                     | Toda adaptación de la UI se realiza con consentimiento explícito y reversible. | El usuario puede decidir si desea recibir guía, activar el modo de lectura o personalizar la visualización. |
| **Privacidad por diseño**                                    | Protección de datos personales desde el diseño.              | Los modelos procesan solo metadatos de uso (sin datos bancarios ni biométricos). |
| **No discriminación**                                        | Evitar sesgos por edad, discapacidad, lengua o nivel educativo. | El sistema adapta el lenguaje, los íconos y los colores al perfil del usuario, sin clasificarlo de forma excluyente. |
| **Explicabilidad y transparencia**                           | Las decisiones de la IA deben ser entendibles.               | La app muestra frases como “Te sugerimos esto porque detectamos dificultad para leer el texto”. |
| **Beneficio directo al usuario**                             | Maximizar beneficios, minimizar riesgos.                     | Se prioriza prevenir fraudes y brindar confianza, no monetizar el comportamiento del usuario. |
| **Justicia social**                                          | Reducir brechas de acceso y uso.                             | B-Accesible busca beneficiar especialmente a las comunidades rurales, a las personas adultas mayores y a las personas con discapacidad. |
| **Robustez y seguridad**                                     | Debe fucionar de manera segura y previsible                  | Se busca implementar controles de validación de entrada y el uso de pruebas  controladas para detectar fallos antes de producción. [^15] |
| **Rendición de cuentas**                                     | Personas físicas o jurídicas responsables del uso de la IA deben  poder ser identificadas y responder por su correcto funcionamiento, así como  por daños ocasionados. | Mantener  un registro de auditorías éticas y técnicas sobre el comportamiento del  módulo (por  ejemplo, el nudging ético o las adaptaciones personalizadas). [^15] |
| **Crecimiento inclusivo, desarrollo sostenible y bienestar** | Debe contribuir al progreso social y económico de forma  inclusiva, ayudando a reducir desigualdades y promoviendo el desarrollo  humano. | Implementación  de interfaces accesibles  para personas con discapacidad, así como su comprensión por personas mayores o con bajo nivel digital. También se busca que su uso contribuya a la reducción de la brecha  digital. [^15] |



## ⚖️ Persuasión Ética (Nudging Responsable)

El sistema incluye un **motor de “nudges” adaptativos** que orienta al usuario en tiempo real:

- Detecta patrones de confusión (errores repetidos, pausas largas).  

- Preserva la autonomía del usuario[^6]

- Ofrece ayuda sin imponerla:  
  > “¿Deseas que te guíe paso a paso?”  
  
- Mantiene un tono respetuoso, sin lenguaje técnico ni infantilización.  

- No se usa con fines comerciales ni para manipular decisiones financieras.

- Transparencia y publicidad del nudge [^6]

  - Cada intervención va acompañada de una breve explicación
  - No se ocultan las motivaciones ni se emplean técnicas persuasivas encubiertas.
  - Busca reducir la tecnofobia y aumentar la confianza digital, ofreciendo asistencia empática sin presión ni juicio. 


---

## 🔐 Privacidad y Seguridad Digital

1. **Datos mínimos:** solo se recopilan datos de interacción (tiempo, errores, navegación).  
2. **Anonimización completa** en los conjuntos de datos de entrenamiento (sintéticos).  
3. **Cifrado de comunicación** (HTTPS) y tokens temporales para sesiones.  
4. **Auditoría ética de IA:** las predicciones se documentan junto con su propósito y la versión del modelo.  
5. **Alineación con la LFPDPPP**: no se recaban ni transfieren datos personales sensibles.  
6. **Derechos digitales reconocidos:**
   - *Derecho a la libertad de sesgo.*  
   - *Derecho a la explicabilidad.*  
   - *Derecho a la privacidad contextual.*
   - *Derecho a la inclusión digital*.
   - *Derecho a la educación digital.*

---

## ♿ Accesibilidad Universal

El diseño cumple con las **Pautas WCAG 2.1, nivel AA,** y considera el marco **EN 301 549** sobre accesibilidad para TIC.

**Elementos implementados:**

- Modos de alto contraste y texto grande.  
- Navegación por voz y retroalimentación auditiva.  
- Iconografía culturalmente relevante (símbolos reconocibles en México). [^1] 
- Lenguaje claro.
- Posibilidad de incorporar traducción opcional a **lenguas originarias** (ej. Náhuatl, Mixteco, Zapoteco) a futuro mediante TTS locales. [^1]

---

## 💡 Impacto Social Esperado

| Eje                                                | Contribución                                                 |
| -------------------------------------------------- | ------------------------------------------------------------ |
| **Inclusión financiera**                           | Brinda acceso a operaciones básicas de banca móvil a poblaciones sin experiencia digital. |
| **Reducción de fraudes**                           | IA preventiva que alerta sobre comportamientos sospechosos, contribuyendo a prevenir fraudes coercitivos. |
| **Educación financiera inclusiva**                 | Usa términos financieros comunes mediante ejemplos hablados. |
| **Autonomía digital y reducción de la tecnofobia** | Se promueve confianza en la tecnología a través de orientación paso a paso, lenguaje empático y educación digital gradual. Se busca que las personas superen el miedo o la desconfianza hacia las herramientas digitales, transformando la ansiedad tecnológica en experiencias de aprendizaje seguras y significativas |



---

## 🧠 Transparencia Algorítmica

Cada modelo (nudging, accesibilidad, riesgo) se desarrolla bajo los principios de transparencia, explicabilidad y equidad, garantizando decisiones responsables y libres de sesgos [^16].

**Dataset sintético documentado:** cada modelo se entrena con datos diversos y representativos, y se documentan variables, sesgos y limitaciones. Los conjuntos se actualizan y se auditan regularmente para garantizar la equidad.

**Versión controlada:** cada modelo indica su versión y la fecha de entrenamiento, lo que permite rastrear los cambios y mantener la transparencia a lo largo de su ciclo de vida.

**Explicaciones simples y comprensibles:** las recomendaciones se expresan en un lenguaje claro para fortalecer la confianza del usuario [^9],[^12].
 *Ejemplo:* “Te recomendamos un texto grande porque indicaste dificultad visual.”

**Código abierto y auditable:** el código fuente está disponible para su revisión técnica y ética, lo que asegura la transparencia y la responsabilidad en la toma de decisiones [^13].

**Monitoreo y mejora continua:** los modelos y sus regulaciones se evalúan y ajustan periódicamente para mantener su equidad, precisión y cumplimiento ético [^13].

Los humanos y las organizaciones siempre son responsables de imbuir a la IA de pautas éticas. El objetivo del enfoque incluye la priorización de la seguridad, la dignidad y el bienestar humanos. Esto también incluye, como mínimo, la ley de Asimov, que establece que la IA no puede dañar a ningún ser humano ni, por inacción, permitir que algún ser humano sufra daño [^17].

---

## 🧾 Licencia Ética

El proyecto se distribuye bajo licencia **MIT con cláusula ética complementaria**, que prohíbe su uso en:

- Actividades de vigilancia o coerción.  
- Sistemas que discriminen o exploten vulnerabilidades.  
- Aplicaciones comerciales que manipulen decisiones financieras o políticas.

---

## ✅ Cumplimiento de principios éticos

| Criterio                | Cumplimiento | Evidencia                                            |
| ----------------------- | ------------ | ---------------------------------------------------- |
| Privacidad por diseño   | ✅            | Datos anonimizados, sin identificadores personales.  |
| Accesibilidad universal | ✅            | Contraste, texto grande, guiado por voz.             |
| Persuasión ética        | ✅            | Nudging responsable, lenguaje claro.                 |
| Explicabilidad          | ✅            | Mensajes transparentes y trazabilidad de decisiones. |
| Inclusión social        | ✅            | Enfoque en grupos marginados y rurales.              |
| Seguridad               | ✅            | Cifrado, prevención de fraude.                       |
| Transparencia de IA     | ✅            | Modelos documentados y abiertos.                     |
| Respeto cultural        | ✅            | Iconografía y lenguaje contextual mexicano.          |

---

## 📚 Referencias

[^1]: Breaking Accessibility Barriers Through Laughter: An Emotional and Universal Design Approach to Address Technophobia in Augmented Reality”, doi: 10.1007/978-3-031-93851-1_8.
[^2]: Calderón, C. (2024, June 18). *El analfabetismo digital afecta a 23% de los internautas que hay en México*. El Financiero. https://www.elfinanciero.com.mx/empresas/2024/06/18/el-analfabetismo-digital-afecta-a-23-de-los-internautas-que-hay-en-mexico/
[^3]: CNBV (2022). Reporte de Inclusión Financiera en México. 
[^4]: De Felipe, A., Puerto, C., Benemérito, D., Proletariado, R., Del Mayab, D., De, L., Senadora, A. L., & Soto, R. I. D. G. (n.d.). *De la Senadora Alejandra Lagunes Soto Ruíz integrante del Grupo Parlamentario*. Alejandralagunes.Mx. Retrieved November 11, 2025, from https://www.alejandralagunes.mx/_files/ugd/447d95_5da6b430111b4f3384f0f4a29768b39e.pdf
[^5]: De Felipe, A., Puerto, C., Benemérito, D., Proletariado, R., Del Mayab, D., De, L., Senadora, A. L., & Soto, R. I. D. G. (n.d.-a). *COMISIÓN PERMANENTE DEL H. CONGRESO DE LA UNIÓN LXV LEGISLATURA*. Alejandralagunes.Mx. Retrieved November 11, 2025, from https://www.alejandralagunes.mx/_files/ugd/447d95_70f0e750fb4242df98bf5b325ea2ba04.pdf
[^6]: Ethical Considerations of Digital Nudging based on its Behavioural Economics Roots (Lembcke, Engelbrecht, Brendel & Kolbe, 2019)
[^7]: INEGI (2023). Encuesta Nacional sobre Disponibilidad y Uso de Tecnologías de la Información en los Hogares (ENDUTIH). 
[^8]: Inspirado en el enfoque de Nudge Theory de Thaler & Sunstein (2008), reinterpretado desde la perspectiva de la IA centrada en el ser humano (Human-Centered AI).
[^9]: M. A. Falk, “Causes and Coping Strategies for Technology Anxiety Among the Elderly in the Digital Age,” *Journal of research in social science and humanities*, vol. 3, no. 10, pp. 6–11, Oct. 2024, doi: 10.56397/jrssh.2024.10.02.
[^10]: M. E. Beutel *et al.*, “Verminderung von Technologieängsten in der psychosomatischen Rehabilitation—Konzepte und Ergebnisse zu einem Computertraining für ältere Arbeitnehmer*,” *Zeitschrift Fur Gerontologie Und Geriatrie*, vol. 37, no. 3, pp. 221–230, June 2004, doi: 10.1007/S00391-004-0184-7.
[^11]: Menlo Report (2012). Ethical Principles Guiding Information and Communication Technology Research. 
[^12]: N. Selwyn, “Teaching Information Technology to the ‘Computer Shy’: A Theoretical Perspective on a Practical Problem.,” *Journal of Vocational Education & Training*, vol. 49, no. 3, pp. 395–408, Sept. 1997, doi: 10.1080/13636829700200023.
[^13]: Ridzuan, N. N., Masri, M., Anshari, M., Fitriyani, N. L., & Syafrudin, M. (2024). AI in the Financial Sector: The Line between Innovation, Regulation and Ethical Responsibility. *Information*, *15*(8), 432. https://doi.org/10.3390/info15080432
[^14]: Secretaría de Economía (2021). Estrategia Digital Nacional y Carta de Derechos Digitales. 
[^15]: Senado de la República (México). (2025). Propuesta de Marco Normativo para la Inteligencia Artificial (IA) en México. https://comisiones.senado.gob.mx/inteligencia_artificial/images/noticias/Propuesta.pdf
[^16]: Thaler, R., & Sunstein, C. (2008). Nudge: Improving Decisions About Health, Wealth, and Happiness.
[^17]: Tóth, Z., & Blut, M. (2024). Ethical compass: The need for Corporate Digital Responsibility in the use of Artificial Intelligence in financial services. *Organizational Dynamics*, *53*(2), 101041. https://doi.org/10.1016/j.orgdyn.2024.101041
[^18]: UNESCO (2021). Recomendación sobre la Ética de la Inteligencia Artificial. 

> 💬 *“En México, la inclusión digital no empieza con la conectividad, sino con el diseño accesible y ético que reconozca la diversidad humana.”*