import spacy
from spacy import displacy

from spacy import displacy
MODEL_PATH = 'models/disease_model'
ner = spacy.load(MODEL_PATH)
text = "Selegiline - induced postural hypotension in Parkinson ' s disease : a longitudinal study on the effects of drug withdrawal.The aims of this study were to confirm our previous findings in a separate cohort of patients and to determine the time course of the cardiovascular consequences of stopping selegiline in the expectation that this might shed light on the mechanisms by which the drug causes orthostatic hypotension"
doc = ner(text)
# displacy.render(doc,jupyter=True, style = "ent")
displacy.serve(doc, style="ent")

