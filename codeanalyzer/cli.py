import argparse
import sys
import os
import shutil
from .utils import download_repo, scan_files
from .analyzer import CodeAnalyzer


def setup_command(args):
    print("Initializing code analyzer...")
    with open(".env", "w") as f:
        f.write("DEEPSEEK_API_KEY=your_api_key_here\n")
    print("Setup complete. Edit .env file with your actual API key.")


def analyze_command(args):
    print(f"\n🔍 Starting analysis of {args.github_url}")
    repo_path = None
    try:
        # Phase 1: Download
        repo_path = download_repo(args.github_url)

        # Phase 2: Scan
        files = scan_files(repo_path)
        print(f"📁 Found {len(files)} files to analyze")

        # Phase 3: Analyze
        analyzer = CodeAnalyzer()
        analyzer.analyze_project(files)

        # Phase 4: Report
        report = analyzer.generate_report()

        print("\n📝 Final Summary:")
        print("=" * 80)
        print(report['summary'])

        if report['detailed_findings']:
            print("\n🔍 Detailed Findings:")
            for finding in report['detailed_findings']:
                print(f"\nFile: {finding['file']}")
                print("-" * 80)
                print(finding['result'])
        else:
            print("\n✅ No significant issues found")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)
    finally:
        if repo_path and os.path.exists(os.path.dirname(repo_path)):
            shutil.rmtree(os.path.dirname(repo_path))


def main():
    parser = argparse.ArgumentParser(prog="code_analyzer")
    subparsers = parser.add_subparsers()

    setup_parser = subparsers.add_parser('setup', help='Initial setup')
    setup_parser.set_defaults(func=setup_command)

    analyze_parser = subparsers.add_parser('analyze', help='Analyze a repository')
    analyze_parser.add_argument('github_url', help='GitHub repository URL')
    analyze_parser.set_defaults(func=analyze_command)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()