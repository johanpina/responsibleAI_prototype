MODEL_CARD_HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Model Card</title>
<style>
    body {{
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      color: #333;
      margin: 0;
      padding: 0;
      background-color: #eaeaea;
    }}
    .container {{
      max-width: 800px;
      margin: auto;
      background-color: #fff;
      padding: 20px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }}
    .column-container {{
      column-count: 2;
      column-gap: 40px;
    }}
    h1 {{
      color: #007bff;
      font-size: 22px;
      text-align: center;
      margin-bottom: 24px;
      column-span: all; /* Hace que el título se extienda a través de todas las columnas */
    }}
    h2, p, ul, li {{
      font-size: 14px;
      color: #333;
      line-height: 1.6;
    }}
    .footer {{
    font-size: 12px;
    text-align: center;
    margin-top: 20px;
    color: #666;
   }}
    @media screen and (max-width: 768px) {{
      .column-container {{
        column-count: 1; /* Cambia a una sola columna para pantallas más pequeñas */
      }}
    }}
  </style>
</head>
<body>
<div class="container">
  <h1>{Nombre_modelo}</h1>
  <div class="column-container">
    <div class="column">
      <h2>Detalles del Modelo</h2>
      <ul>
        <li>Modelo desarrollado por: {desarrollador_modelo} </li>
        <li>Versión del modelo: {version_modelo} </li>
        <li>Fecha de implementación: {fecha_modelo} </li>
        <li>{tipo_modelo}</li>
        <li>Enlace {link_modelo}</li>
        <li>¿Cómo citar?: {cita_modelo}</li>
        <li>Licencia del modelo: {licencia_modelo}</li>
        <li>Contacto: {contacto_modelo}</li>
      </ul>

      <h2>Visión general del modelo</h2>
      <ul>
        <li>{proposito_modelo}</li>
        <li>{TA_porque_modelo}</li>
        <li>{TA_alcanzar_resultados}</li>
        <li>{UsoPrevisto_modelo}</li>
        <li>{UsosNocontext_modelo}</li>
      </ul>

      <!-- Este es el render de TA que está pendiente para agregar-->
      <!--TODO: acá debo revisar atributos para poder ocultar secciones que en el formulario el usuario las tiene en NO,
        debo enviar el valor del atributo-->

      <h2>Transparencia activa</h2>
      <ul>
        <li>{TA_datos_modelo}</li>
        <li>{TA_datos_entrenamiento_modelo}</li>
        <li>{TA_datos_evaluacion_modelo}</li>
        <li>{TA_datos_justicia_modelo}</li>
        <li>{TA_datos_advertencias_modelo}</li>
      </ul>

      <!--FIN BLOQUE TA-->
    
      <h2>Métricas de rendimiento</h2>
      <p>{metricas_modelo}</p>
      <ul>
        <li>Umbral de decisión: {umbralDesicion_modelo}</li>
      </ul>
      <p>{calculo_mediciones_modelo}</p>
      
      <h2>Datos de Entrenamiento</h2>
      <p>{datos_modelo}</p>
      <p>{preprocesamiento_modelo}</p>

      <h2>Datos de Evaluación</h2>
      <p>{conjunto_datos_eval_modelo}</p>
      <p>{eleccion_evaluacion}</p>
      <p>{preprocesamiento_evaluacion}</p>


      <h2>Consideraciones Éticas</h2>
      <p>¿Este modelo categoriza las personas?: {TA_modelo_categoriza}</p> <!--PREGUNTAR A MARIANA COMO DEBEMOS MOSTRAR ESTO-->
      <p>{TA_razones_decision_negativa_personas}</p>
      <p>¿El modelo usa datos personales?: {TA_datos_personales}</p> <!--CAmbiar a checkbox-->
      <p>{TA_razones_datos_personales}</p>

      <p>Datos sensibles: {dato_sensible_tipo}</p>
      <p>Decisiones sobre asuntos centrales: {asuntos_centrales_tipo}</p>

      <p>{estrategias_mitigaciones_modelo}</p>
      <p>{riesgos_uso_modelo}</p>
      <p>{casos_uso_conocidos}</p>
      <p>{otra_consideracion}</p>

      <h2>Advertencias y Recomendaciones</h2>
      <p>{prueba_adicional}</p>
      <p>{grupo_relevante}</p>
      <p>{recomendaciones_adicionales}</p>
      <p>{caracteristicas_ideales}</p>
      <p>{TA_via_reclamacion}</p>


    </div>
  </div>
</div>
<div class="footer">
    <p>© {year} Instituto GobLab. Todos los derechos reservados.</p>
    <p>Esta Model Card fue elaborada en {elaboration_date}.</p>
</div>
</body>
</html>

"""