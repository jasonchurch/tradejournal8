import subprocess
import sys
import yaml
import os
from pathlib import Path
parent_folder = Path(__file__).resolve().parent.parent.parent
#cli_path = Path(__file__).resolve().parent.parent / "cli.py"

def test_cli_runs(tmp_path):
    # Prepare config
    config = {
        "watch_folder": str(tmp_path),
        "mask_output_folder": str(tmp_path / "masked"),
        "file_pattern": "*.pdf",
        "poll_interval": 1,
    }
    cfg_file = tmp_path / "config.yaml"
    cfg_file.write_text(yaml.dump(config))

    # Prepare dummy pdf
    pdf = tmp_path / "in.pdf"
    pdf.write_text("FAKE PDF")

    # Run CLI with timeout
    result = subprocess.run(
        [sys.executable, "-m", "trademaskerfilewatcher.cli", "--config", str(cfg_file)],
        capture_output=True,
        text=True,
        timeout=5,
        env={**os.environ, "PYTHONPATH": str(parent_folder)}
    )

    # Verify CLI output
    assert "New file detected" in result.stdout
    assert "_masked.pdf" in result.stdout
