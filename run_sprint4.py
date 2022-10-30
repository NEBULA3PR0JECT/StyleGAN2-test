# from nebula3_experts.experts.pipeline.api import PipelineApi, PipelineTask
import os
# from typing import Tuple

def find(d, tag):
    if tag in d:
        yield d[tag]
    for k, v in d.items():
        if isinstance(v, dict):
            for i in find(v, tag):
                yield i

def test_pipeline_task(pipeline_id):
    class MyTask(PipelineTask):
        def process_movie(self, movie_id: str) -> Tuple[bool, str]:
            print (f'handling movie: {movie_id}')
            # task actual work
            print(" Hello World. ")
            return True, None
        def get_name(self) -> str:
            return "my-task"

    pipeline = PipelineApi(None)
    task = MyTask()
    pipeline.handle_pipeline_task(task, pipeline_id, stop_on_failure=True)

def test():
    pipeline_id = os.environ.get('PIPELINE_ID')
    print(pipeline_id)
    # test_pipeline_task(pipeline_id)

if __name__ == '__main__':
    test()
