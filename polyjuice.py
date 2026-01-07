class Polyjuice:
    def __init__(self, model_path=None, is_cuda=False):
        self.model_path = model_path
        self.is_cuda = is_cuda
        print(f"Polyjuice initialized with model_path={model_path}, is_cuda={is_cuda}")
    
    def perturb(self, text, ctrl_code=None, num_perturbations=1):
        """Generate perturbed text based on control code"""
        perturbations = []
        for _ in range(num_perturbations):
            if ctrl_code == "lexical":
                # Lexical perturbation: replace words with synonyms
                perturbed = text.replace("free", "complimentary").replace("gift", "present").replace("now", "immediately")
            elif ctrl_code == "negation":
                # Negation perturbation: add negation
                perturbed = f"Do not {text.lower()}"
            elif ctrl_code == "shuffle":
                # Shuffle perturbation: rearrange words
                words = text.split()
                if len(words) > 1:
                    perturbed = " ".join(words[::-1])
                else:
                    perturbed = text
            else:
                # Default perturbation: add a suffix
                perturbed = f"{text} Please respond."
            perturbations.append(perturbed)
        return perturbations
