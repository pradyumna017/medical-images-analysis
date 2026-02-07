from datetime import datetime

def build_pacs_json(patient_id, analysis, heatmap_path):
    return {
        "schema_version": "1.0",
        "modality": "XRAY",

        "patient": {
            "patient_id": patient_id,
            "deidentified": True
        },

        "analysis_results": {
            "abnormality_detection": analysis
        },

        "outputs": {
            "heatmap_path": heatmap_path
        },

        "compliance": {
            "analysis_only": True,
            "no_diagnosis": True,
            "no_treatment": True
        },

        "audit": {
            "timestamp": datetime.utcnow().isoformat()
        }
    }
