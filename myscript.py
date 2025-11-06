# myscript.py
import os

GOOD = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"  # stable
BAD  = "c1a4be04b972b6c17db242fc37752ad517c29402"  # cassé

os.system("git bisect reset > /dev/null 2>&1")
os.system(f"git bisect start {BAD} {GOOD}")
os.system("git bisect run python manage.py test")
os.system("git bisect reset")