import yaml
from fastapi import HTTPException


async def get_tasks_for_build(build_name):
    with open('./builds/builds.yaml') as f:
        builds = yaml.safe_load(f)
    with open('./builds/tasks.yaml') as f:
        tasks = yaml.safe_load(f)

    result = []
    current_build = [x for x in builds['builds'] if x['name'] == build_name]
    if len(current_build) == 0:
        raise HTTPException(status_code=404, detail='no such build')
    for current_task in current_build[0]['tasks']:
        await add_task(tasks, current_task, result)

    return result


async def add_task(tasks, current_task, result):
    filtered_task = list(filter(lambda x: x['name'] == current_task, tasks['tasks']))
    if len(filtered_task) == 0:
        raise HTTPException(status_code=404, detail='no such task ' + current_task)
    if len(filtered_task[0]['dependencies']) > 0:
        for t in filtered_task[0]['dependencies']:
            await add_task(tasks, t, result)
    if current_task not in result:
        result.append(current_task)

# def main():
#     try:
#         result = get_tasks_for_build('forward_interest')
#         print(result)
#     except Exception as e:
#         print(e)
#
#
# if __name__ == "__main__":
#     main()
