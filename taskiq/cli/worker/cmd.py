import logging
from typing import Optional, Sequence

from taskiq.abc.cmd import TaskiqCMD
from taskiq.cli.worker.args import WorkerArgs
from taskiq.cli.worker.run import run_worker

logger = logging.getLogger(__name__)


class WorkerCMD(TaskiqCMD):
    """Command to run workers."""

    short_help = "Helper to run workers"

    def exec(self, args: Sequence[str]) -> Optional[int]:
        """
        Start worker process.

        Worker process creates several small
        processes in which tasks are actually processed.

        :param args: CLI arguments.
        :returns: status code.
        """
        logging.getLogger("taskiq").setLevel(level=logging.getLevelName(logging.INFO))
        logging.getLogger("watchdog.observers.inotify_buffer").setLevel(level=logging.INFO)
        logger.info(f"TaskIQ Worker startup args: {", ".join(args)}")
        wargs = WorkerArgs.from_cli(args)
        logger.info(f"TaskIQ Worker --workers after processing: {wargs.workers}")
        return run_worker(wargs, args)
