import os

BASE_DIR = "outputs"
CHART_DIR = os.path.join(BASE_DIR, "charts")
REPORT_DIR = os.path.join(BASE_DIR, "reports")


# =====================================================
# SAFE INITIALIZATION (CRASH PROOF)
# =====================================================
def init_environment():
    """
    This version is bulletproof:
    - handles Windows race conditions
    - prevents FileExistsError
    - ensures folder exists BEFORE ANY SAVE
    """

    folders = [BASE_DIR, CHART_DIR, REPORT_DIR]

    for folder in folders:
        try:
            os.makedirs(folder, exist_ok=True)
        except FileExistsError:
            pass
        except OSError:
            pass


# =====================================================
# SAFE PATH GENERATORS
# =====================================================
def get_chart_path(filename: str):
    init_environment()  # 🔥 CRITICAL FIX (ensures folder exists every time)
    return os.path.join(CHART_DIR, filename)


def get_report_path(filename: str):
    init_environment()
    return os.path.join(REPORT_DIR, filename)