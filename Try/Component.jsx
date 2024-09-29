import Link from "next/link"
import { Tabs, TabsList, TabsTrigger, TabsContent, TabsItem } from "@/components/ui/tabs"
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from "@/components/ui/card"
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"

export default function Component() {
  return (
    <div className="flex flex-col h-screen">
      <header className="bg-primary text-primary-foreground py-4 px-6">
        <div className="flex items-center justify-between max-w-6xl mx-auto">
          <h1 className="text-2xl font-bold">PII Detector</h1>
          <nav>
            <ul className="flex items-center space-x-4">
              <li>
                <Link href="#" prefetch={false}>
                  Home
                </Link>
              </li>
              <li>
                <Link href="#" prefetch={false}>
                  Upload
                </Link>
              </li>
              <li>
                <Link href="#" prefetch={false}>
                  Redact
                </Link>
              </li>
              <li>
                <Link href="#" prefetch={false}>
                  About
                </Link>
              </li>
            </ul>
          </nav>
        </div>
      </header>
      <main className="flex-1 bg-background text-foreground p-8">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold mb-4">Detect and Redact PII</h2>
          <p className="text-muted-foreground mb-8">
            Upload documents to identify and remove government-issued personally identifiable information
            (PII).
          </p>
          <Tabs>
            <TabsList>
              <TabsTrigger>Upload</TabsTrigger>
              <TabsTrigger>Enter Data</TabsTrigger>
            </TabsList>
            <TabsContent>
              <div>
                <Card className="p-6">
                  <CardHeader>
                    <CardTitle>Upload Document</CardTitle>
                    <CardDescription>Select a file to scan for PII.</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <form>
                      <div className="mb-4">
                        <Label htmlFor="file">File</Label>
                        <Input id="file" type="file" />
                      </div>
                      <Button type="submit">Scan for PII</Button>
                    </form>
                  </CardContent>
                </Card>
              </div>
              <div>
                <Card className="p-6">
                  <CardHeader>
                    <CardTitle>Enter Data</CardTitle>
                    <CardDescription>Input personal information to check for PII.</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <form>
                      <div className="mb-4">
                        <Label htmlFor="name">Name</Label>
                        <Input id="name" type="text" />
                      </div>
                      <div className="mb-4">
                        <Label htmlFor="email">Email</Label>
                        <Input id="email" type="email" />
                      </div>
                      <div className="mb-4">
                        <Label htmlFor="pan">PAN</Label>
                        <Input id="pan" type="text" />
                      </div>
                      <div className="mb-4">
                        <Label htmlFor="aadhaar">Aadhaar</Label>
                        <Input id="aadhaar" type="text" />
                      </div>
                      <Button type="submit">Scan for PII</Button>
                    </form>
                  </CardContent>
                </Card>
              </div>
            </TabsContent>
          </Tabs>
        </div>
      </main>
      <footer className="bg-muted text-muted-foreground py-4 px-6">
        <div className="max-w-6xl mx-auto text-center">
          <p>&copy; 2023 PII Detector. All rights reserved.</p>
        </div>
      </footer>
    </div>
  )
}