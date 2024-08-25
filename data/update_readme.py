import json
import argparse
import os

def generate_readme(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        test_cases = json.load(f)

    readme_content = """
# LLM Test Cases / LLM 测试用例

This repository contains a collection of test cases for evaluating Large Language Models (LLMs).
此仓库包含用于评估大型语言模型（LLMs）的测试用例集合。

<details>
<summary>View Test Cases / 查看测试用例</summary>

<div id="test-cases">
"""

    for case in test_cases:
        readme_content += f"""
  <div class="test-case">
    <h3>{case['title']} / {case['title_zh']}</h3>
    <p><strong>Description:</strong> {case['description']}</p>
    <p><strong>描述：</strong>{case['description_zh']}</p>
    <p><strong>Prompt:</strong> {case['prompt']}</p>
    <p><strong>提示：</strong>{case['prompt_zh']}</p>
    <hr>
  </div>
"""

    readme_content += """
</div>

<style>
#test-cases {
  font-family: Arial, sans-serif;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 8px;
}
.test-case {
  background-color: white;
  padding: 15px;
  margin-bottom: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}
h3 {
  color: #333;
  margin-top: 0;
}
hr {
  border: none;
  border-top: 1px solid #eee;
  margin: 15px 0;
}
</style>

</details>
"""

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(readme_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate README from test cases JSON')
    parser.add_argument('--input', help='Path to the input JSON file')
    parser.add_argument('--output', help='Path to the output README file')
    args = parser.parse_args()

    generate_readme(args.input, args.output)