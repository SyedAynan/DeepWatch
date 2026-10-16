Define and run a reproducible experiment: $ARGUMENTS

Steps:
1. Read docs/DATASET_AND_EXPERIMENT_PLAN.md for experiment design constraints
2. Define the experiment:
   - Hypothesis (what are we testing?)
   - Independent variables (what changes between runs?)
   - Dependent variables / metrics (what do we measure?)
   - Control conditions (baseline comparison)
   - Dataset(s) and split strategy
   - Random seed(s): use 42, 123, 456 for 3-run averaging
3. Create/update an experiment config in eval/ as JSON or YAML
4. Implement the evaluation script if it doesn't exist
5. Check resource requirements BEFORE running (GPU memory, disk, estimated time)
6. Run the experiment with logging
7. Collect results: metrics, confusion matrices, timing
8. Compare against baselines and prior results in docs/MEMORY.md

Do NOT download large datasets or run GPU-intensive training without confirming resource availability.
Report all results honestly — negative results are valuable.
