import streamlit as st
from datetime import datetime

# Configuración de la página
st.set_page_config(
    page_title="TRAMAS - Autogestión y Digitalización",
    page_icon="🕸️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS personalizado
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 2rem;
    }
    .stProgress > div > div > div > div {
        background-color: #667eea;
    }
    .welcome-box {
        background-color: #EFF6FF;
        border-left: 4px solid #3B82F6;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    .info-box {
        background-color: #F3F4F6;
        border-left: 4px solid #6B7280;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #ECFDF5;
        border: 2px solid #10B981;
        padding: 2rem;
        border-radius: 8px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Inicializar session state
if 'page' not in st.session_state:
    st.session_state.page = 0
if 'num_organizaciones' not in st.session_state:
    st.session_state.num_organizaciones = 0
if 'num_proyectos' not in st.session_state:
    st.session_state.num_proyectos = 0
if 'current_entity' not in st.session_state:
    st.session_state.current_entity = 0
if 'organizaciones' not in st.session_state:
    st.session_state.organizaciones = []
if 'proyectos' not in st.session_state:
    st.session_state.proyectos = []
if 'herramientas_admin' not in st.session_state:
    st.session_state.herramientas_admin = {}
if 'herramientas_digitales' not in st.session_state:
    st.session_state.herramientas_digitales = {}
if 'demograficos' not in st.session_state:
    st.session_state.demograficos = {}

# Header
st.markdown("""
<div class="main-header">
    <h1>🕸️ TRAMAS</h1>
    <p style="margin: 0;">Tejidos en Red: Análisis y Mapeos Sociales</p>
</div>
""", unsafe_allow_html=True)

# Barra de progreso
total_pages = 6
progress = st.session_state.page / total_pages
st.progress(progress)
st.caption(f"Progreso: {int(progress * 100)}%")

# ==================== PÁGINA 0: BIENVENIDA ====================
def page_bienvenida():
    st.markdown("## Bienvenida")
    
    st.markdown("""
    <div class="welcome-box">
        <p>En el mundo del arte, la cultura y el emprendimiento social las personas solemos participar en múltiples espacios, proyectos u organizaciones. Esto lo hacemos por necesidades financieras en muchos casos, pero también por exploraciones estéticas, sociales o personales.</p>
        
        <p>Definitivamente, no todos los productos o proyectos que hacemos pueden enmarcarse en un solo lugar, y por eso tenemos que dividirlos. Eso plantea grandes retos para la gestión de cada uno, especialmente afectados hoy en día por la digitalización. En este mapa queremos conocer de qué manera divides tu trabajo, qué necesidades de gestión tienes y cómo estás apropiando herramientas digitales.</p>
        
        <p><strong>Te agradecemos tu participación.</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 Iniciar Encuesta", use_container_width=True, type="primary"):
        st.session_state.page = 1
        st.rerun()

# ==================== PÁGINA 1: CANTIDAD ====================
def page_cantidad():
    st.markdown("## Parte 1: Organizaciones y Proyectos")
    
    st.markdown("""
    <div class="info-box">
        <p>Una <strong>organización</strong> la consideramos como un espacio con límites claramente definidos, con división de labores o funciones y mecanismos de pertenencia establecidos. Tienen una conformación formal a partir de mecanismos de legalización como pueden ser empresas, organizaciones públicas, instituciones educativas, asociaciones civiles, corporaciones, colectivos conformados formalmente, entre otros.</p>
        
        <p>Un <strong>proyecto</strong>, en cambio, no tiene del todo una conformación formal necesariamente, pueden participar múltiples personas y organizaciones sin que tengan un mecanismo de membresía establecido pero enfocados en el desarrollo de un producto específico como puede ser un disco, una obra de teatro, una exposición de arte, una película, entre otros.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### ¿Actualmente a cuántas organizaciones y proyectos perteneces?")
    st.caption("Ten en cuenta que deberás responder la encuesta por cada uno que incluyas en tu respuesta")
    
    col1, col2 = st.columns(2)
    
    with col1:
        num_org = st.number_input("Organizaciones:", min_value=0, max_value=20, value=st.session_state.num_organizaciones, key="input_org")
    
    with col2:
        num_proy = st.number_input("Proyectos:", min_value=0, max_value=20, value=st.session_state.num_proyectos, key="input_proy")
    
    if num_org + num_proy > 0:
        if st.button("Continuar ➡️", use_container_width=True, type="primary"):
            st.session_state.num_organizaciones = num_org
            st.session_state.num_proyectos = num_proy
            st.session_state.organizaciones = [{} for _ in range(num_org)]
            st.session_state.proyectos = [{} for _ in range(num_proy)]
            st.session_state.current_entity = 0
            st.session_state.page = 2
            st.rerun()
    else:
        st.warning("⚠️ Debes agregar al menos una organización o proyecto para continuar.")

# ==================== PÁGINA 2: ENTIDADES ====================
def page_entidades():
    total_entities = st.session_state.num_organizaciones + st.session_state.num_proyectos
    current = st.session_state.current_entity
    
    # Determinar si es organización o proyecto
    is_org = current < st.session_state.num_organizaciones
    
    if is_org:
        entity_index = current
        entity_type = "Organización"
        entity_data = st.session_state.organizaciones[entity_index]
        st.markdown(f"## {entity_type} {entity_index + 1}")
    else:
        entity_index = current - st.session_state.num_organizaciones
        entity_type = "Proyecto"
        entity_data = st.session_state.proyectos[entity_index]
        st.markdown(f"## {entity_type} {entity_index + 1}")
    
    st.caption(f"Entidad {current + 1} de {total_entities}")
    
    with st.form(key=f"entity_form_{current}"):
        if is_org:
            tipo = st.selectbox(
                "Tipo de organización:",
                ["Selecciona...", "Emprendimiento", "Empresa pequeña (menos de 50 personas)", 
                 "Empresa mediana (entre 50 y 100 personas)", "Empresa grande (más de 100 personas)",
                 "Organización pública", "Organización educativa pública", "Organización educativa privada",
                 "Asociación civil", "Corporación", "Colectivo"],
                index=0 if entity_data.get('tipo') is None else ["Selecciona...", "Emprendimiento", "Empresa pequeña (menos de 50 personas)", 
                 "Empresa mediana (entre 50 y 100 personas)", "Empresa grande (más de 100 personas)",
                 "Organización pública", "Organización educativa pública", "Organización educativa privada",
                 "Asociación civil", "Corporación", "Colectivo"].index(entity_data.get('tipo', 'Selecciona...'))
            )
            cargo = st.text_input("Cargo o rol:", value=entity_data.get('cargo', ''), placeholder="Ej: Director, Coordinador, Miembro...")
        else:
            nombre = st.text_input("Nombre del proyecto:", value=entity_data.get('nombre', ''), placeholder="Nombre del proyecto")
            cargo = st.text_input("Cargo, función o rol:", value=entity_data.get('cargo', ''), placeholder="Ej: Productor, Artista, Colaborador...")
        
        col1, col2 = st.columns(2)
        with col1:
            prev_button = st.form_submit_button("⬅️ Anterior", use_container_width=True)
        with col2:
            next_button = st.form_submit_button("Siguiente ➡️" if current < total_entities - 1 else "Continuar ➡️", 
                                               use_container_width=True, type="primary")
        
        if prev_button:
            if current > 0:
                st.session_state.current_entity -= 1
                st.rerun()
            else:
                st.session_state.page = 1
                st.rerun()
        
        if next_button:
            # Guardar datos
            if is_org:
                st.session_state.organizaciones[entity_index] = {'tipo': tipo, 'cargo': cargo}
            else:
                st.session_state.proyectos[entity_index] = {'nombre': nombre, 'cargo': cargo}
            
            if current < total_entities - 1:
                st.session_state.current_entity += 1
                st.rerun()
            else:
                st.session_state.page = 3
                st.rerun()

# ==================== PÁGINA 3: HERRAMIENTAS ADMIN ====================
def page_herramientas_admin():
    st.markdown("## Herramientas Administrativas y Gestivas")
    
    # Preparar lista de entidades
    all_entities = []
    for i, org in enumerate(st.session_state.organizaciones):
        all_entities.append(('org', i, f"Organización {i+1}"))
    for i, proy in enumerate(st.session_state.proyectos):
        nombre = proy.get('nombre', f"Proyecto {i+1}")
        all_entities.append(('proy', i, nombre))
    
    if len(all_entities) > 1:
        entity_names = [e[2] for e in all_entities]
        selected_entity = st.selectbox("Responder para:", entity_names)
        entity_idx = entity_names.index(selected_entity)
        entity_type, entity_index, _ = all_entities[entity_idx]
    else:
        entity_type, entity_index, _ = all_entities[0]
    
    # Obtener datos guardados
    entity_key = f"{entity_type}_{entity_index}"
    if entity_key not in st.session_state.herramientas_admin:
        st.session_state.herramientas_admin[entity_key] = {}
    
    data = st.session_state.herramientas_admin[entity_key]
    
    with st.form("herramientas_form"):
        jerarquia = st.selectbox(
            "1. Tipo de jerarquía de la organización:",
            ["Selecciona...", "Altamente jerarquizada", "Tiene menos de 3 niveles jerárquicos",
             "No tiene jerarquías", "Nos repartimos los liderazgos y funciones"],
            index=0 if not data.get('jerarquia') else ["Selecciona...", "Altamente jerarquizada", "Tiene menos de 3 niveles jerárquicos",
             "No tiene jerarquías", "Nos repartimos los liderazgos y funciones"].index(data.get('jerarquia', 'Selecciona...'))
        )
        
        planeacion = st.selectbox(
            "2. Forma de planeación:",
            ["Selecciona...", "Se hace un plan estratégico periódico y se revisa por las personas directivas",
             "Se hace un plan estratégico y se comunica de manera oficial",
             "Se hace un plan estratégico pero no se comunica",
             "Todas las personas participan en el desarrollo del plan estratégico",
             "No tiene ninguna planeación"],
            index=0 if not data.get('planeacion') else ["Selecciona...", "Se hace un plan estratégico periódico y se revisa por las personas directivas",
             "Se hace un plan estratégico y se comunica de manera oficial",
             "Se hace un plan estratégico pero no se comunica",
             "Todas las personas participan en el desarrollo del plan estratégico",
             "No tiene ninguna planeación"].index(data.get('planeacion', 'Selecciona...'))
        )
        
        ecosistema = st.selectbox(
            "3. Ecosistema:",
            ["Selecciona...", "Participamos formalmente con otras organizaciones de diferentes sectores",
             "Participamos informalmente con organizaciones de diferentes sectores pero las reconocemos",
             "Participamos formal o informalmente con organizaciones o proyectos del mismo sector",
             "No reconocemos participación con nadie más"],
            index=0 if not data.get('ecosistema') else ["Selecciona...", "Participamos formalmente con otras organizaciones de diferentes sectores",
             "Participamos informalmente con organizaciones de diferentes sectores pero las reconocemos",
             "Participamos formal o informalmente con organizaciones o proyectos del mismo sector",
             "No reconocemos participación con nadie más"].index(data.get('ecosistema', 'Selecciona...'))
        )
        
        redes = st.selectbox(
            "4. Redes:",
            ["Selecciona...", "Reconocemos organizaciones de nuestro mismo sector y participamos activamente con ellas",
             "Reconocemos activamente a las organizaciones del sector pero no nos reconocen",
             "Nos falta generar lazos mucho más fuertes pero los estamos consolidando",
             "No participamos con nadie"],
            index=0 if not data.get('redes') else ["Selecciona...", "Reconocemos organizaciones de nuestro mismo sector y participamos activamente con ellas",
             "Reconocemos activamente a las organizaciones del sector pero no nos reconocen",
             "Nos falta generar lazos mucho más fuertes pero los estamos consolidando",
             "No participamos con nadie"].index(data.get('redes', 'Selecciona...'))
        )
        
        funciones = st.selectbox(
            "5. Funciones y labores:",
            ["Selecciona...", "Tenemos funciones y roles claramente identificados y bajo contrato",
             "Tenemos funciones y roles identificados y formalizados",
             "Tenemos funciones y roles repartidos de manera informal pero identificables",
             "Tenemos roles informales un poco fluidos",
             "No tenemos roles todas las personas aportan por igual"],
            index=0 if not data.get('funciones') else ["Selecciona...", "Tenemos funciones y roles claramente identificados y bajo contrato",
             "Tenemos funciones y roles identificados y formalizados",
             "Tenemos funciones y roles repartidos de manera informal pero identificables",
             "Tenemos roles informales un poco fluidos",
             "No tenemos roles todas las personas aportan por igual"].index(data.get('funciones', 'Selecciona...'))
        )
        
        liderazgo = st.selectbox(
            "6. Liderazgo:",
            ["Selecciona...", "Existen líderes específicos para cada área",
             "Existen líderes específicos según el proyecto",
             "Nos repartimos el liderazgo por conocimiento y experiencia",
             "No tenemos un liderazgo muy claro"],
            index=0 if not data.get('liderazgo') else ["Selecciona...", "Existen líderes específicos para cada área",
             "Existen líderes específicos según el proyecto",
             "Nos repartimos el liderazgo por conocimiento y experiencia",
             "No tenemos un liderazgo muy claro"].index(data.get('liderazgo', 'Selecciona...'))
        )
        
        identidad = st.selectbox(
            "7. Identidad:",
            ["Selecciona...", "Tiene una marca claramente definida incluso con manual de marca",
             "Tiene una marca claramente definida pero la identidad es más informal",
             "Tiene una marca y la identidad es fluida",
             "Tiene una marca pero la identidad es bastante fluida",
             "Tenemos una marca específica para cada línea de trabajo",
             "No tiene una identidad de ningún tipo"],
            index=0 if not data.get('identidad') else ["Selecciona...", "Tiene una marca claramente definida incluso con manual de marca",
             "Tiene una marca claramente definida pero la identidad es más informal",
             "Tiene una marca y la identidad es fluida",
             "Tiene una marca pero la identidad es bastante fluida",
             "Tenemos una marca específica para cada línea de trabajo",
             "No tiene una identidad de ningún tipo"].index(data.get('identidad', 'Selecciona...'))
        )
        
        col1, col2 = st.columns(2)
        with col1:
            prev_button = st.form_submit_button("⬅️ Anterior", use_container_width=True)
        with col2:
            next_button = st.form_submit_button("Siguiente ➡️", use_container_width=True, type="primary")
        
        if prev_button:
            st.session_state.page = 2
            st.session_state.current_entity = len(all_entities) - 1
            st.rerun()
        
        if next_button:
            st.session_state.herramientas_admin[entity_key] = {
                'jerarquia': jerarquia,
                'planeacion': planeacion,
                'ecosistema': ecosistema,
                'redes': redes,
                'funciones': funciones,
                'liderazgo': liderazgo,
                'identidad': identidad
            }
            st.session_state.page = 4
            st.rerun()

# ==================== PÁGINA 4: HERRAMIENTAS DIGITALES ====================
def page_herramientas_digitales():
    st.markdown("## Uso de Herramientas Digitales")
    
    with st.form("digitales_form"):
        st.markdown("### 1. De las siguientes, ¿qué herramientas utilizas?")
        herramientas = st.multiselect(
            "Selecciona todas las que apliquen:",
            ["Redes sociales", "Almacenamiento en la nube", 
             "Banca en línea (recibimos pagos por terminal, datáfono, transferencia, botón de pago en línea, etc)",
             "Banca en línea (no recibimos pagos)", "Correo personalizado",
             "Plataformas de llamadas o reuniones virtuales", "Paquetería o software de oficina",
             "Paquetería avanzada o especializada"],
            default=st.session_state.herramientas_digitales.get('herramientas', [])
        )
        
        herramientas_pagadas = []
        if herramientas:
            st.markdown("### 2. De esas herramientas, ¿cuáles pagas?")
            herramientas_pagadas = st.multiselect(
                "Selecciona las que pagas:",
                herramientas,
                default=st.session_state.herramientas_digitales.get('herramientas_pagadas', [])
            )
        
        st.markdown("### 3. ¿Qué inteligencias artificiales utilizas?")
        ias = st.multiselect(
            "Selecciona todas las que apliquen:",
            ["ChatGPT, Gemini, Claude, Perplexity u otro generador de texto",
             "Grammarly, Deepl Write u otros asistentes de escritura o de búsqueda",
             "Deepl Translate, Google Translate u otros asistentes de traducción",
             "Copilot, Notion AI u otros asistentes integrados en programas de oficina",
             "Adobe Firefly, DALL-E, Midjourney, Leonardo AI, Wondershare u otros generadores de imágenes o videos",
             "Khanmigo, Duolingo Max u otros tutores o herramienta pedagógica",
             "Wolfram Alpha, MATHGPT u otras herramientas para resolver problemas matemáticos",
             "Noodel Factory, Gradescope u otras plataformas educativas",
             "Woebot, Wysa Replika u otras herramientas de apoyo emocional",
             "GitHub Copilot, Claude Code, Replit AI, Tabnine u otras herramientas para escribir o corregir código de programación",
             "Otras", "Ninguna"],
            default=st.session_state.herramientas_digitales.get('ias', [])
        )
        
        ias_pagadas = []
        if ias and "Ninguna" not in ias:
            st.markdown("### 4. ¿De esas herramientas pagas alguna?")
            ias_sin_ninguna = [ia for ia in ias if ia != "Ninguna"]
            ias_pagadas = st.multiselect(
                "Selecciona las que pagas:",
                ias_sin_ninguna,
                default=st.session_state.herramientas_digitales.get('ias_pagadas', [])
            )
        
        st.markdown("### 5. ¿Perteneces a alguna comunidad en línea?")
        comunidades = st.multiselect(
            "Selecciona todas las que apliquen:",
            ["Grupos de WhatsApp o Telegram", "Grupos de difusión de WhatsApp o Telegram",
             "Grupos de redes sociales", "Comunidades especializadas con contacto en línea (por ejemplo: Twitch)",
             "Comunidades especializadas con contacto en línea y presencial"],
            default=st.session_state.herramientas_digitales.get('comunidades', [])
        )
        
        col1, col2 = st.columns(2)
        with col1:
            prev_button = st.form_submit_button("⬅️ Anterior", use_container_width=True)
        with col2:
            next_button = st.form_submit_button("Siguiente ➡️", use_container_width=True, type="primary")
        
        if prev_button:
            st.session_state.page = 3
            st.rerun()
        
        if next_button:
            st.session_state.herramientas_digitales = {
                'herramientas': herramientas,
                'herramientas_pagadas': herramientas_pagadas,
                'ias': ias,
                'ias_pagadas': ias_pagadas,
                'comunidades': comunidades
            }
            st.session_state.page = 5
            st.rerun()

# ==================== PÁGINA 5: DEMOGRÁFICOS ====================
def page_demograficos():
    st.markdown("## Datos Demográficos")
    
    st.warning("⚠️ Los campos marcados con * son obligatorios")
    
    with st.form("demograficos_form"):
        st.markdown("### Información obligatoria")
        
        pais = st.text_input("País *", value=st.session_state.demograficos.get('pais', ''), 
                             placeholder="Ej: Colombia, México")
        ciudad = st.text_input("Ciudad *", value=st.session_state.demograficos.get('ciudad', ''),
                               placeholder="Ej: Bogotá, Ciudad de México")
        edad = st.selectbox("Rango de edad *",
                           ["Selecciona...", "18-24 años", "25-34 años", "35-44 años", 
                            "45-54 años", "55-64 años", "65+ años"],
                           index=0 if not st.session_state.demograficos.get('edad') else 
                           ["Selecciona...", "18-24 años", "25-34 años", "35-44 años", 
                            "45-54 años", "55-64 años", "65+ años"].index(st.session_state.demograficos.get('edad', 'Selecciona...')))
        nivel_academico = st.selectbox("Nivel académico *",
                                      ["Selecciona...", "Sin estudios formales", "Primaria", "Secundaria",
                                       "Preparatoria/Bachillerato", "Técnico", "Licenciatura/Grado",
                                       "Maestría/Posgrado", "Doctorado"],
                                      index=0 if not st.session_state.demograficos.get('nivel_academico') else
                                      ["Selecciona...", "Sin estudios formales", "Primaria", "Secundaria",
                                       "Preparatoria/Bachillerato", "Técnico", "Licenciatura/Grado",
                                       "Maestría/Posgrado", "Doctorado"].index(st.session_state.demograficos.get('nivel_academico', 'Selecciona...')))
        
        st.markdown("### Información opcional")
        
        nombre = st.text_input("Nombre", value=st.session_state.demograficos.get('nombre', ''),
                              placeholder="Opcional")
        correo = st.text_input("Correo electrónico", value=st.session_state.demograficos.get('correo', ''),
                              placeholder="Opcional")
        telefono = st.text_input("Teléfono", value=st.session_state.demograficos.get('telefono', ''),
                                placeholder="Opcional")
        entrevista = st.radio("¿Quisieras que te contactemos para ampliar el estudio con entrevistas en profundidad?",
                             ["No especificado", "Sí", "No"],
                             index=0 if not st.session_state.demograficos.get('entrevista') else
                             ["No especificado", "Sí", "No"].index(st.session_state.demograficos.get('entrevista', 'No especificado')))
        convocatorias = st.multiselect("¿Quisieras participar en alguna de las siguientes convocatorias?",
                                      ["Talleres de autogestión", "Ferias de arte o divulgación"],
                                      default=st.session_state.demograficos.get('convocatorias', []))
        
        col1, col2 = st.columns(2)
        with col1:
            prev_button = st.form_submit_button("⬅️ Anterior", use_container_width=True)
        with col2:
            submit_button = st.form_submit_button("✅ Finalizar Encuesta", use_container_width=True, type="primary")
        
        if prev_button:
            st.session_state.page = 4
            st.rerun()
        
        if submit_button:
            if not pais or not ciudad or edad == "Selecciona..." or nivel_academico == "Selecciona...":
                st.error("⚠️ Por favor completa todos los campos obligatorios")
            else:
                st.session_state.demograficos = {
                    'pais': pais,
                    'ciudad': ciudad,
                    'edad': edad,
                    'nivel_academico': nivel_academico,
                    'nombre': nombre,
                    'correo': correo,
                    'telefono': telefono,
                    'entrevista': entrevista,
                    'convocatorias': convocatorias,
                    'timestamp': datetime.now().isoformat()
                }
                
                # TODO: Aquí se guardaría en Google Sheets
                
                st.session_state.page = 6
                st.rerun()

# ==================== PÁGINA 6: GRACIAS ====================
def page_gracias():
    st.markdown("""
    <div class="success-box">
        <h2>✅ ¡Gracias por tu participación!</h2>
        <p style="font-size: 1.1rem; margin-top: 1rem;">Tus respuestas han sido registradas exitosamente.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🔄 Realizar otra encuesta", use_container_width=True, type="primary"):
        # Reiniciar todo
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# ==================== ROUTING ====================
if st.session_state.page == 0:
    page_bienvenida()
elif st.session_state.page == 1:
    page_cantidad()
elif st.session_state.page == 2:
    page_entidades()
elif st.session_state.page == 3:
    page_herramientas_admin()
elif st.session_state.page == 4:
    page_herramientas_digitales()
elif st.session_state.page == 5:
    page_demograficos()
elif st.session_state.page == 6:
    page_gracias()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6B7280; font-size: 0.9rem; padding: 1rem;">
    <p>TRAMA es una plataforma desarrollada por <strong>El Chorro Producciones</strong> y <strong>Huika Mexihco</strong></p>
</div>
""", unsafe_allow_html=True)